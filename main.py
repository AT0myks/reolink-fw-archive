#!/usr/bin/env python3

import asyncio
import itertools
import json
import re
from datetime import date, datetime
from operator import itemgetter
from zoneinfo import ZoneInfo

import aiohttp
from dateutil.parser import parse as dtparse
from lxml.html import document_fromstring, fragment_fromstring, tostring
from lxml.html.builder import OL, LI
from reolinkfw import get_info
from waybackpy import WaybackMachineCDXServerAPI

WAYBACK_MAX_CONN = 20
FILE_DEVICES = "devices.json"
FILE_PAKINFO = "pak_info.json"
FILE_FW_LIVE = "firmwares_live.json"
FILE_FW_MANL = "firmwares_manual.json"
FILE_FW_ARV2 = "firmwares_archives_support.json"


async def get_one(session, url, type_="text"):
    async with session.get(url) as resp:
        return await (resp.json() if type_ == "json" else resp.text())


async def get_all(urls, type_="text", limit_per_host=0):
    conn = aiohttp.TCPConnector(limit_per_host=limit_per_host)
    async with aiohttp.ClientSession(connector=conn) as session:
        return await asyncio.gather(*[get_one(session, url, type_) for url in urls])


def load_devices():
    with open(FILE_DEVICES, 'r', encoding="utf8") as f:
        return json.load(f)


def load_firmwares():
    # live must be first because its information takes precedence. 
    with (open(FILE_FW_LIVE, 'r', encoding="utf8") as live,
            open(FILE_FW_ARV2, 'r', encoding="utf8") as arv2,
            open(FILE_FW_MANL, 'r', encoding="utf8") as man):
        return json.load(live) + json.load(arv2) + json.load(man)


def load_pak_info():
    with open(FILE_PAKINFO, 'r', encoding="utf8") as f:
        return json.load(f)


def md_link(label, url):
    return f"[{label}]({url})"


def make_changes(changes):
    if not changes:
        return ''
    elif len(changes) == 1:
        return changes[0]
    items = []
    subitems = []
    for idx, i in enumerate(changes):
        if i[0].isdigit() or i[0].isupper():
            items.append(LI(re.sub("^[0-9\s\W]{2,4}", '', i)))
        elif i[0].islower():
            subitems.append(LI(re.sub("^[a-z\s\W]{2,3}", '', i)))
            if (idx + 1) == len(changes) or not changes[idx + 1][0].islower():  # If end of list or next item is not a subitem.
                items[-1].append(OL(*subitems, type='a'))
                subitems = []  # Reset.
    return tostring(OL(*items)).decode()


def make_title(device):
    title = device["title"].removesuffix(" (NVR)")
    if (type_ := device.get("type", "IPC")) != "IPC":
        title += f" ({type_})"
    if device.get("discontinued"):
        title += " *"
    return title


def parse_build_date(build_date):
    return date(2000 + int(build_date[:2]), int(build_date[2:4]), int(build_date[4:]))


def make_readme(firmwares):
    pak_info = load_pak_info()
    def sort(tup):
        return tup[1]["info"]["build_date"]
    text = ''
    devices = sorted(load_devices(), key=itemgetter("title"))
    for model in devices:
        text += "<details>\n  <summary>" + make_title(model) + "</summary>\n"
        if prodimg := model.get("productImg"):
            text += f'\n<img src="{prodimg}" width="150">\n'
        if produrl := model.get("productUrl"):
            text += '\n' + md_link("Product page", produrl) + '\n'
        for hv in model["hardwareVersions"]:
            text += "\n  ### " + hv["title"] + "\n"
            text += "Version | Date | Changes | Notes\n"
            text += "--- | --- | --- | ---\n"
            for sha, pi in sorted(((k, v) for k, v in pak_info.items() if v["model_id"] == model["id"] and v["hw_ver_id"] == hv["id"] if not v["info"].get("error")), key=sort, reverse=True):
                fws = [fw for fw in firmwares if fw["sha256_pak"] == sha]
                # If a firmware appears both in live and archivesv2, the live instance
                # will appear first in the list and therefore be the one selected.
                fw = fws[0] if fws else {}
                info = pi["info"]
                links = []
                for url in sorted(pi["download"]):
                    dl_url = url
                    if "filename" in fw and "wp-content" in url:
                        dl_url += "?download_name=" + fw["filename"]
                    ver = info["firmware_version_prefix"] + '.' + info["version_file"]
                    links.append(md_link(ver, dl_url))
                version = "<br />".join(links)
                dt = parse_build_date(info["build_date"])
                date_str = str(dt).replace('-', chr(0x2011))
                new = make_changes(fw.get("changelog"))
                notes = []
                if pi.get("beta"):
                    notes.append(":warning: This is a beta firmware")
                if note := fw.get("note"):
                    notes.extend(note.split('\n'))
                if "archive_url" in fw:
                    notes.append(md_link("Archive", fw["archive_url"]))
                for nb, url in enumerate(fw.get("source_urls", []), start=1):
                    notes.append(md_link(f"Source {nb}", url))
                notes = "<br />".join(notes)
                text += " | ".join((version, date_str, new, notes)) + '\n'
        text += "\n</details>\n\n"
    return text


def sanitize(string):
    return string.translate({
        160: ' ',  # \xa0
        183: '',  # \u00b7
        8217: "'",  # \u2019
        8220: '"',  # \u201c
        8221: '"',  # \u201d
    }).strip()


def parse_changes(text):
    text = sanitize(text)
    text = text.removeprefix("<p>").removesuffix("</p>")
    text = text.removeprefix("<P>").removesuffix("</P>")
    return re.split("\s*</?[pP]>\s*<[pP]>\s*|\s*<br />\s*", text)


def parse_timestamps(display_time, updated_at):
    """For live firmwares."""
    dt = display_time / 1000
    sh = ZoneInfo("Asia/Shanghai")
    tz = sh if datetime.fromtimestamp(dt, sh).hour == 0 else ZoneInfo("UTC")
    return datetime.fromtimestamp(dt, tz), datetime.fromtimestamp(updated_at / 1000, tz)


async def from_live_website():
    async with aiohttp.ClientSession() as session:
        devices = (await get_one(session, "https://reolink.com/wp-json/reo-v2/download/product/selection-list", "json"))["data"]
    urls = [f"https://reolink.com/wp-json/reo-v2/download/firmware/?dlProductId={dev['id']}" for dev in devices]
    firmwares = []
    for response in await get_all(urls, "json"):
        for data in response["data"]:
            for fw in data["firmwares"]:
                hw_ver = fw["hardwareVersion"][0]
                note = fragment_fromstring(fw["note"], create_parent=True).text_content()
                fw["firmware_id"] = fw.pop("id")
                fw["hw_ver_id"] = hw_ver["id"]
                fw["model_id"] = hw_ver["dlProduct"]["id"]
                fw["note"] = sanitize(note)
                fw["url"] = fw["url"].replace("%2F", '/')
                fw["model"] = hw_ver["dlProduct"]["title"]
                fw["hw_ver"] = hw_ver["title"].strip()
                fw["changelog"] = parse_changes(fw.pop("new"))
                fw["display_time"], fw["updated_at"] = parse_timestamps(fw.pop("displayTime"), fw["updated_at"])
                del fw["hardwareVersion"]
                if fw not in firmwares:
                    firmwares.append(fw)
    return devices, firmwares


async def get_archives_v1_firmware_links(limit_per_host=WAYBACK_MAX_CONN):
    """Return a list of unique firmware download links."""
    cdx = WaybackMachineCDXServerAPI("reolink.com", filters=["statuscode:200", "original:.*/firmware/.*", "mimetype:text/html"], match_type="host")
    snapshots = (snap.archive_url for snap in cdx.snapshots())
    links = []
    for response in await get_all(snapshots, limit_per_host=limit_per_host):
        doc = document_fromstring(response)
        for a in doc.iter("a"):
            href = a.get("href")
            if href is not None and ".zip" in href:
                link = "http" + href.split("http")[-1]
                if link not in links:  # Keep order, don't use a set.
                    links.append(link)
    return links


def parse_old_support_page_changes(text):
    match = re.search("(?:\s*What's new:?)?(.*?)(?:Note:|Before upgrading)", text, re.DOTALL)
    if not match:
        return []
    new = match.group(1).strip()
    by_lf = new.split('\n')
    by_nb = re.split("[0-9]{1,2}\. ", new)[1:]
    # If lengths are equal, take by_nb because it's the one without the numbers.
    return [sanitize(t) for t in (by_lf if len(by_lf) > len(by_nb) else by_nb)]


async def get_and_parse_old_support_page(session, url):
    """For https://support.reolink.com/hc/en-us/articles/ pages."""
    html = await get_one(session, url)
    doc = document_fromstring(html)
    main = doc.find("./body/main")
    title = doc.find("./head/title").text
    # Could also use date in link or in firmware.
    dt = dtparse(title.split("Firmware")[0]).date()
    for body in main.find_class("article-body"):
        if new := parse_old_support_page_changes(body.text_content()):
            break
    firmwares = []
    for table in main.findall(".//table"):
        for tr in table.iter("tr"):
            if len(tr) == 2:
                model, firmware = tr
                hardware = None
            elif len(tr) == 3:
                model, firmware, hardware = tr
            elif len(tr) == 4:
                model, firmware, _, hardware = tr
            if "model" in model.text_content().lower():
                continue  # Ignore table header.
            a = firmware.find(".//a")  # xpath because some pages have the <a> under a span, and also multiple <a>s with different links????
            firmwares.append({
                "model": sanitize(model.text_content()),
                "version": sanitize(a.text_content()),
                "hw_ver": sanitize(hardware.text_content()) if hardware is not None else None,
                "display_time": dt,
                "url": "http" + a.get("href").split("http")[-1],
                "changelog": new,
                "archive_url": url
            })
    return firmwares


async def from_support_archives(limit_per_host=WAYBACK_MAX_CONN):
    cdx = WaybackMachineCDXServerAPI("https://support.reolink.com/hc/en-us/articles/*", filters=["statuscode:200", "original:.*[0-9]-Firmware-for.*"], collapses=["digest"])
    urls = set(snap.archive_url for snap in cdx.snapshots())
    conn = aiohttp.TCPConnector(limit_per_host=limit_per_host)
    async with aiohttp.ClientSession(connector=conn) as session:
        lists = await asyncio.gather(*[get_and_parse_old_support_page(session, url) for url in urls])
    return [fw for firmwares in lists for fw in firmwares]


def clean_model(model):
    return model.removesuffix("-5MP").removesuffix(" (NVR)").replace(' ', '-').lower()


def clean_hw_ver(hw_ver):
    return hw_ver.replace('-', '_').strip()


def get_model_id(devices, model):
    for dev in devices:
        if clean_model(dev["title"]) == clean_model(model):
            return dev["id"]
    return None


def get_hw_ver_id(devices, model_id, hw_ver_names):
    if (idx := get_item_index(devices, "id", model_id)) is None:
        return None
    hw_vers = devices[idx]["hardwareVersions"]
    # Try exact match first.
    for hw_ver in hw_vers:
        for name in hw_ver["title"].split(" or "):
            clean = clean_hw_ver(name)
            if any(clean_hw_ver(name) == clean for name in hw_ver_names):
                return hw_ver["id"]
    # Then substring.
    for hw_ver in hw_vers:
        for name in hw_ver["title"].split(" or "):
            clean = clean_hw_ver(name)
            if any(clean_hw_ver(name).startswith(clean) for name in hw_ver_names):
                return hw_ver["id"]
    return None


def match(pak_info):
    if "error" in pak_info:
        return None, None
    devices = load_devices()
    model_id = get_model_id(devices, pak_info["display_type_info"])
    keys = ("board_type", "detail_machine_type", "board_name")
    hw_names = set(pak_info[key] for key in keys)
    hw_ver_id = get_hw_ver_id(devices, model_id, hw_names)
    return model_id, hw_ver_id


def update_ids(pak_info, old_model_id, old_hw_id, new_model_id, new_hw_id):
    if (old_model_id, old_hw_id) == (None, None):
        return
    for key in pak_info:
        if pak_info[key]["model_id"] == old_model_id and old_model_id is not None:
            pak_info[key]["model_id"] = new_model_id
        if pak_info[key]["hw_ver_id"] == old_hw_id and old_hw_id is not None:
            pak_info[key]["hw_ver_id"] = new_hw_id


def add_pak_info(pak_info, model_id=None, hw_ver_id=None):
    pak_infos = load_pak_info()
    if model_id is None or hw_ver_id is None:  # They should always be both None or not.
        model_id, hw_ver_id = match(pak_info)
    else:
        # This code is only reached in case of a live firmware (both ids are present).
        # In case a device/hw version was previously manually added and then
        # matched for at least one pak file, update it/them with the "official" ids.
        old_model_id, old_hw_ver_id = match(pak_info)
        update_ids(pak_infos, old_model_id, old_hw_ver_id, model_id, hw_ver_id)
    copy = pak_info.copy()
    sha = copy.pop("sha256")
    url = copy.pop("url")
    if sha in pak_infos:
        if url not in pak_infos[sha]["download"]:
            pak_infos[sha]["download"].append(url)
    else:
        pak_infos[sha] = {
            "info": copy,
            "download": [url],
            "model_id": model_id,
            "hw_ver_id": hw_ver_id
        }
    with open(FILE_PAKINFO, 'w', encoding="utf8") as f:
        json.dump(pak_infos, f, indent=2)


def add_and_clean(pak_infos, dicts=[], source=None):
    """Add new firmware info to FILE_PAKINFO and return cleaned up firmwares."""
    firmwares = []
    for fw, infos in itertools.zip_longest(dicts, pak_infos, fillvalue={}):
        fw.pop("url", None)
        model_id = fw.pop("model_id", None)
        hw_ver_id = fw.pop("hw_ver_id", None)
        for info in infos:
            if "sha256" in info:
                add_pak_info(info, model_id, hw_ver_id)
                firmwares.append({**fw, "sha256_pak": info["sha256"], "source": source})
            else:
                firmwares.append({**fw, **info, "source": source})
    return firmwares


def keep_most_recent(firmwares):
    """Return a list containing only the most recent snapshot for each unique firmware file link."""
    urls = {fw["url"] for fw in firmwares}
    return [sorted((fw for fw in firmwares if fw["url"] == url), key=itemgetter("archive_url"))[-1] for url in urls]


async def add_archives_v1_firmwares(limit_per_host=WAYBACK_MAX_CONN):
    urls = await get_archives_v1_firmware_links(limit_per_host)
    pak_infos = await asyncio.gather(*[get_info(url) for url in urls])
    add_and_clean(pak_infos)


async def create_support_archives_firmwares(limit_per_host=WAYBACK_MAX_CONN):
    firmwares = await from_support_archives(limit_per_host=limit_per_host)
    filtered = keep_most_recent(firmwares)
    pak_infos = await asyncio.gather(*[get_info(fw["url"]) for fw in filtered])
    clean_fws = add_and_clean(pak_infos, filtered, "archives_v2")
    with open(FILE_FW_ARV2, 'w', encoding="utf8") as f:
        json.dump(clean_fws, f, indent=2, default=str)


async def create_live_devices_and_firmwares():
    devices, firmwares = await from_live_website()
    with open(FILE_DEVICES, 'w', encoding="utf8") as f:
        json.dump(devices, f, indent=2)
    pak_infos = await asyncio.gather(*[get_info(fw["url"]) for fw in firmwares])
    clean_fws = add_and_clean(pak_infos, firmwares, "live")
    with open(FILE_FW_LIVE, 'w', encoding="utf8") as f:
        json.dump(clean_fws, f, indent=2, default=str)


async def add_archives_v3_firmwares():
    existingurls = {url for val in load_pak_info().values() for url in val["download"]}
    prefixes = [
        "https://reolink.com/firmware/",
        "https://cdn.reolink.com/files/firmware/",
        "https://home-cdn.reolink.us/files/firmware/",
        "https://home-cdn.reolink.us/wp-content/uploads/",
        "https://s3.amazonaws.com/reolink-storage/website/firmware/",
        "https://reolink-storage.s3.amazonaws.com/website/firmware/"
    ]
    urls = set()
    for prefix in prefixes:
        cdx = WaybackMachineCDXServerAPI(prefix + '*', filters=["original:.*\.zip"])
        for snap in cdx.snapshots():
            url = snap.original.replace("%2F", '/').split('?')[0]
            if url not in existingurls:
                urls.add(url)
    pak_infos = await asyncio.gather(*[get_info(url) for url in urls])
    # The errors here are ZIPs that don't contain any PAKs (PDFs...).
    add_and_clean([pi for pi in pak_infos if "error" not in pi[0]])


def get_item_index(items, key, value):
    """Return the index of the first item in items that has this value for this key.
    
    The key must exist in each item. Return None if no match is found.
    """
    for idx, item in enumerate(items):
        if item[key] == value:
            return idx
    return None


def merge_dicts(old, new):
    """Update old with data from new. Modify old in-place.
    
    This is not 100% generic and is mostly intended to be used in this project.
    """
    for key, val in new.items():
        if key in ("url", "model_id", "hw_ver_id"):  # For live firmware merging.
            continue
        if old.get(key) != val:
            if key in ("productImg", "productUrl"):  # For device merging.
                if val:  # Avoid replacing manually set value by an empty live value.
                    old[key] = val
            elif isinstance(val, dict):
                if not isinstance(old.get(key), dict):
                    old[key] = {}
                merge_dicts(old[key], val)
            elif isinstance(val, list):
                if not isinstance(old.get(key), list):
                    old[key] = []
                merge_lists(old[key], val)
            else:
                old[key] = val


def merge_lists(old, new, key="title"):
    """Modify old in-place. Non generic."""
    for item in new:
        if item in old:
            continue
        elif isinstance(item, dict) and (idx := get_item_index(old, key, item[key])) is not None:
            merge_dicts(old[idx], item)
        else:
            old.append(item)


async def update_live_info():
    devices_new, firmwares_new = await from_live_website()
    devices_old = load_devices()
    with open(FILE_FW_LIVE, 'r', encoding="utf8") as fw:
        firmwares_old = json.load(fw)
    old_len = len(firmwares_old)  # The new firmwares will start at the end of the list.
    merge_lists(devices_old, devices_new)  # Hoping the titles don't change.
    merge_lists(firmwares_old, firmwares_new, "firmware_id")
    pak_infos = await asyncio.gather(*[get_info(fw["url"]) for fw in firmwares_old[old_len:]])
    firmwares_old[old_len:] = add_and_clean(pak_infos, firmwares_old[old_len:], "live")
    with open(FILE_DEVICES, 'w', encoding="utf8") as f:
        json.dump(devices_old, f, indent=2)
    with open(FILE_FW_LIVE, 'w', encoding="utf8") as f:
        json.dump(firmwares_old, f, indent=2, default=str)


async def add_firmwares_manually():
    """If a new device/hw ver is involved, it must be added manually first."""
    with open(FILE_FW_MANL, 'r', encoding="utf8") as f:
        firmwares = json.load(f)
    new = []
    while firmwares and "url" in firmwares[-1]:
        new.append(firmwares.pop())
    pak_infos = await asyncio.gather(*[get_info(fw["url"]) for fw in new])
    firmwares.extend(add_and_clean(pak_infos, new, "manual"))
    with open(FILE_FW_MANL, 'w', encoding="utf8") as f:
        json.dump(firmwares, f, indent=2)


def write_readme():
    with open("README.md", 'w', encoding="utf8") as f:
        f.write(make_readme(load_firmwares()))


if __name__ == "__main__":
    import argparse

    def add():
        asyncio.run(add_firmwares_manually())
        write_readme()

    def update():
        asyncio.run(update_live_info())
        write_readme()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True, title="commands")
    parser_a = subparsers.add_parser("add", help=f"add firmwares that have been manually appended to {FILE_FW_MANL!r}")
    parser_a.set_defaults(func=add)
    parser_u = subparsers.add_parser("update", help="get new firmwares from Reolink and update all files")
    parser_u.set_defaults(func=update)

    args = parser.parse_args()
    args.func()
