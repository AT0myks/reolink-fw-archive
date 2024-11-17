#!/usr/bin/env python3

import asyncio
import itertools
import json
import re
from argparse import ArgumentParser, Namespace
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence
from datetime import datetime
from operator import itemgetter
from typing import Any, Optional
from zoneinfo import ZoneInfo

from aiohttp import ClientSession, TCPConnector
from dateutil.parser import parse as dtparse
from lxml.html import HtmlElement, document_fromstring, fragment_fromstring, tostring
from lxml.html.builder import OL, LI
from reolinkfw import firmware_info
from reolinkfw.typedefs import StrPathURL
from waybackpy import WaybackMachineCDXServerAPI

from common import FILE_DEVICES, clean_hw_ver, get_item_index, get_names, load_devices, match

WAYBACK_MAX_CONN = 20
FILE_PAKINFO = "pak_info.json"
FILE_FW_LIVE = "firmwares_live.json"
FILE_FW_MANL = "firmwares_manual.json"
FILE_FW_ARV2 = "firmwares_archives_support.json"


async def get_one(session: ClientSession, url: str, type_: str = "text") -> Any:
    async with session.get(url, headers={"user-agent": "pyth0n"}) as resp:
        return await (resp.json() if type_ == "json" else resp.text())


async def get_all(urls: Iterable[str], type_: str = "text", limit_per_host: int = 0) -> list[Any]:
    conn = TCPConnector(limit_per_host=limit_per_host)
    async with ClientSession(connector=conn) as session:
        return await asyncio.gather(*[get_one(session, url, type_) for url in urls])


def load_firmwares() -> list[dict[str, Any]]:
    # live must be first because its information takes precedence.
    with (open(FILE_FW_LIVE, 'r', encoding="utf8") as live,
            open(FILE_FW_ARV2, 'r', encoding="utf8") as arv2,
            open(FILE_FW_MANL, 'r', encoding="utf8") as man):
        return json.load(live) + json.load(arv2) + json.load(man)


def load_pak_info() -> dict[str, dict[str, Any]]:
    with open(FILE_PAKINFO, 'r', encoding="utf8") as f:
        return json.load(f)


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})"


def make_changes(changes: Iterable[str]) -> str:
    if not changes:
        return ''
    changes = [change.replace("&nbsp", '') for change in changes]
    if len(changes) == 1:
        return changes[0]
    items: list[HtmlElement] = []
    subitems: list[HtmlElement] = []
    for idx, change in enumerate(changes):
        if change[0].isdigit() or change[0].isupper():
            items.append(LI(re.sub("^[0-9\s\W]{2,4}", '', change)))
        elif change[0].islower():
            subitems.append(LI(re.sub("^[a-z\s\W]{2,3}", '', change)))
            if (idx + 1) == len(changes) or not changes[idx + 1][0].islower():  # If end of list or next item is not a subitem.
                items[-1].append(OL(*subitems, type='a'))
                subitems = []  # Reset.
    return tostring(OL(*items)).decode()


def make_title(device: Mapping[str, Any]) -> str:
    title = device["title"].removesuffix(" (NVR)")
    if (type_ := device.get("type", "IPC")) != "IPC":
        title += f" ({type_})"
    if device.get("discontinued"):
        title += " *"
    return title


def make_readme(firmwares: Iterable[Mapping[str, Any]]) -> str:
    pis = load_pak_info()
    devices = load_devices()
    # Create a model -> hardware version -> PAK info dictionary.
    pak_infos: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for sha, pi in pis.items():
        model_title, hw_title = get_names(devices, pi["model_id"], pi["hw_ver_id"])
        if model_title is None or hw_title is None:
            print("Cannot find a match for", pi["model_id"], '/', pi["hw_ver_id"])
            continue
        pi["sha256"] = sha
        model_title = model_title.strip().removesuffix("-5MP").removesuffix(" (NVR)")
        hw_title = clean_hw_ver(hw_title)
        pak_infos.setdefault(model_title, {}).setdefault(hw_title, []).append(pi)

    def sort_pak_info(pak_info: Mapping[str, Any]) -> tuple[str, str]:
        info = pak_info["info"]
        ver = info["firmware_version_prefix"] + '.' + info["version_file"]
        return (info["build_date"], ver)

    text = f"Total: {len(pis)}\n\n"
    for model in sorted(pak_infos):
        hvs = pak_infos[model]
        model_id = hvs[list(hvs)[0]][0]["model_id"]
        if (device_idx := get_item_index(devices, "id", model_id)) is None:
            print(f"Cannot find device with ID {model_id}")
            continue
        device = devices[device_idx]
        text += "<details>\n  <summary>" + make_title(device) + "</summary>\n"
        if prodimg := device.get("productImg"):
            text += f'\n<img src="{prodimg}" width="150">\n'
        if produrl := device.get("productUrl"):
            text += '\n' + md_link("Product page", produrl) + '\n'
        for hv in sorted(hvs):
            text += "\n  ### " + hv + "\n"
            text += f"\nFirmwares for this hardware version: {len(hvs[hv])}\n\n"
            text += "Version | Date | Changes | Notes\n"
            text += "--- | --- | --- | ---\n"
            for pi in sorted(hvs[hv], key=sort_pak_info, reverse=True):
                fws = [fw for fw in firmwares if fw.get("sha256_pak") == pi["sha256"]]
                # If a firmware appears both in live and archivesv2, the live instance
                # will appear first in the list and therefore be the one selected.
                fw = fws[0] if fws else {}
                info = pi["info"]
                links = []
                for url in sorted(pi["download"]):
                    dl_url = url
                    if "filename" in fw and "wp-content" in url:
                        dl_url += "?download_name=" + fw["filename"] + ".zip"
                    ver = info["firmware_version_prefix"] + '.' + info["version_file"]
                    links.append(md_link(ver, dl_url))
                version = "<br />".join(links)
                dt = datetime.strptime(info["build_date"], "%y%m%d").date()
                date_str = str(dt).replace('-', chr(0x2011))
                new = make_changes(fw.get("changelog", []))
                notes = []
                if pi.get("beta"):
                    notes.append(":warning: This is a beta firmware")
                if pi.get("user_hosted_only"):
                    notes.append(":warning: The only available links for this firmware are hosted by users and not Reolink themselves")
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


def sanitize(string: str) -> str:
    return string.translate({
        160: ' ',  # \xa0
        183: '',  # \u00b7
        8217: "'",  # \u2019
        8220: '"',  # \u201c
        8221: '"',  # \u201d
    }).strip()


def parse_changes(text: str) -> list[str]:
    text = sanitize(text)
    frag = fragment_fromstring(text, True)
    return [text.strip() for text in frag.itertext() if text.strip()]


def parse_timestamps(display_time: int, updated_at: int) -> tuple[datetime, datetime]:
    """For live firmwares."""
    dt = display_time / 1000
    sh = ZoneInfo("Asia/Shanghai")
    tz = sh if datetime.fromtimestamp(dt, sh).hour == 0 else ZoneInfo("UTC")
    return datetime.fromtimestamp(dt, tz), datetime.fromtimestamp(updated_at / 1000, tz)


async def from_live_website() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    async with ClientSession() as session:
        devices = (await get_one(session, "https://reolink.com/wp-json/reo-v2/download/product/selection-list", "json"))["data"]
    urls = [f"https://reolink.com/wp-json/reo-v2/download/firmware/?dlProductId={dev['id']}" for dev in devices]
    firmwares = []
    for response in await get_all(urls, "json"):
        for device in response["data"]:
            for fw in device["firmwares"]:
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


async def get_archives_v1_firmware_links(limit_per_host: int = WAYBACK_MAX_CONN) -> list[str]:
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


def parse_old_support_page_changes(text: str) -> list[str]:
    match = re.search("(?:\s*What's new:?)?(.*?)(?:Note:|Before upgrading)", text, re.DOTALL)
    if not match:
        return []
    new = match.group(1).strip()
    by_lf = new.split('\n')
    by_nb = re.split("[0-9]{1,2}\. ", new)[1:]
    # If lengths are equal, take by_nb because it's the one without the numbers.
    return [sanitize(t) for t in (by_lf if len(by_lf) > len(by_nb) else by_nb)]


async def get_and_parse_old_support_page(session: ClientSession, url: str) -> list[dict[str, Any]]:
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


async def from_support_archives(limit_per_host: int = WAYBACK_MAX_CONN) -> list[dict[str, Any]]:
    cdx = WaybackMachineCDXServerAPI("https://support.reolink.com/hc/en-us/articles/*", filters=["statuscode:200", "original:.*[0-9]-Firmware-for.*"], collapses=["digest"])
    urls = set(snap.archive_url for snap in cdx.snapshots())
    conn = TCPConnector(limit_per_host=limit_per_host)
    async with ClientSession(connector=conn) as session:
        lists = await asyncio.gather(*[get_and_parse_old_support_page(session, url) for url in urls])
    return [fw for firmwares in lists for fw in firmwares]


def update_ids(pak_info: MutableMapping[str, MutableMapping[str, Any]], old_model_id: Optional[int], old_hw_id: Optional[int], new_model_id: int, new_hw_id: int) -> None:
    if (old_model_id, old_hw_id) == (None, None):
        return
    update_model_id = isinstance(old_model_id, int) and old_model_id >= 100000
    update_hw_id = isinstance(old_hw_id, int) and old_hw_id >= 100000
    for key in pak_info:
        if update_model_id and pak_info[key]["model_id"] == old_model_id:
            pak_info[key]["model_id"] = new_model_id
        if update_hw_id and pak_info[key]["hw_ver_id"] == old_hw_id:
            pak_info[key]["hw_ver_id"] = new_hw_id


def add_pak_info(pak_info: dict[str, Any], model_id: Optional[int] = None, hw_ver_id: Optional[int] = None, beta: bool = False, user_hosted_only: bool = False) -> None:
    pak_infos = load_pak_info()
    if model_id is None or hw_ver_id is None:  # They should always be both None or not.
        model_id, hw_ver_id = match(pak_info)
    else:
        # This code is only reached in case of a live firmware (both ids are present).
        # In case a device/hw version was previously manually added and then
        # matched for at least one pak file, update it/them with the "official" ids.
        old_model_id, old_hw_ver_id = match(pak_info)
        update_ids(pak_infos, old_model_id, old_hw_ver_id, model_id, hw_ver_id)  # type: ignore
    copy = pak_info.copy()
    sha = copy.pop("sha256")
    url = copy.pop("file")
    copy.pop("pak")
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
        if beta:
            pak_infos[sha]["beta"] = beta
        if user_hosted_only:
            pak_infos[sha]["user_hosted_only"] = user_hosted_only
    with open(FILE_PAKINFO, 'w', encoding="utf8") as f:
        json.dump(pak_infos, f, indent=2)


def add_and_clean(pak_infos: Iterable[Iterable[dict[str, Any]]], dicts: Iterable[MutableMapping[str, Any]] = [], source: Optional[str] = None) -> list[dict[str, Any]]:
    """Add new firmware info to FILE_PAKINFO and return cleaned up firmwares.

    If there are multiple PAKs in a ZIP, the beta and user_hosted_only
    properties will be applied to all the PAKs, which might not be desired.
    """
    firmwares = []
    for fw, infos in itertools.zip_longest(dicts, pak_infos, fillvalue={}):
        fw.pop("url", None)
        model_id = fw.pop("model_id", None)
        hw_ver_id = fw.pop("hw_ver_id", None)
        beta = fw.pop("beta", False)
        user_hosted_only = fw.pop("user_hosted_only", False)
        for info in infos:
            if "sha256" in info:
                add_pak_info(info, model_id, hw_ver_id, beta, user_hosted_only)
                firmwares.append({**fw, "sha256_pak": info["sha256"], "source": source})
            else:
                firmwares.append({**fw, **info, "source": source})
    return firmwares


def keep_most_recent(firmwares: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return a list containing only the most recent snapshot for each unique firmware file link."""
    urls = {fw["url"] for fw in firmwares}
    return [sorted((fw for fw in firmwares if fw["url"] == url), key=itemgetter("archive_url"))[-1] for url in urls]


async def add_archives_v1_firmwares(limit_per_host: int = WAYBACK_MAX_CONN) -> None:
    urls = await get_archives_v1_firmware_links(limit_per_host)
    pak_infos = await asyncio.gather(*[firmware_info(url) for url in urls])
    add_and_clean(pak_infos)


async def create_support_archives_firmwares(limit_per_host: int = WAYBACK_MAX_CONN) -> None:
    firmwares = await from_support_archives(limit_per_host=limit_per_host)
    filtered = keep_most_recent(firmwares)
    pak_infos = await asyncio.gather(*[firmware_info(fw["url"]) for fw in filtered])
    clean_fws = add_and_clean(pak_infos, filtered, "archives_v2")
    with open(FILE_FW_ARV2, 'w', encoding="utf8") as f:
        json.dump(clean_fws, f, indent=2, default=str)


async def create_live_devices_and_firmwares() -> None:
    devices, firmwares = await from_live_website()
    with open(FILE_DEVICES, 'w', encoding="utf8") as f:
        json.dump(devices, f, indent=2)
    pak_infos = await asyncio.gather(*[firmware_info(fw["url"]) for fw in firmwares])
    clean_fws = add_and_clean(pak_infos, firmwares, "live")
    with open(FILE_FW_LIVE, 'w', encoding="utf8") as f:
        json.dump(clean_fws, f, indent=2, default=str)


async def add_archives_v3_firmwares() -> None:
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
    pak_infos = await asyncio.gather(*[firmware_info(url) for url in urls])
    # The errors here are ZIPs that don't contain any PAKs (PDFs...).
    add_and_clean([pi for pi in pak_infos if "error" not in pi[0]])


def merge_dicts(old: MutableMapping[Any, Any], new: Mapping[Any, Any]) -> None:
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
            elif key == "changelog":  # For live firmware merging.
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


def merge_lists(old: MutableSequence[Any], new: Iterable[Any], key: str = "title") -> None:
    """Modify old in-place. Non generic."""
    for item in new:
        if item in old:
            continue
        elif isinstance(item, dict) and (idx := get_item_index(old, key, item[key])) is not None:
            merge_dicts(old[idx], item)
        else:
            old.append(item)


async def firmware_info_safe(file_or_url: StrPathURL, use_cache: bool = True) -> list[dict[str, Any]]:
    try:
        return await firmware_info(file_or_url, use_cache)
    except Exception as e:
        return [{"file": file_or_url, "error": str(e)}]


async def update_live_info() -> list[list[dict[str, Any]]]:
    devices_new, firmwares_new = await from_live_website()
    devices_old = load_devices()
    with open(FILE_FW_LIVE, 'r', encoding="utf8") as fw:
        firmwares_old: list[dict[str, Any]] = json.load(fw)
    old_len = len(firmwares_old)  # The new firmwares will start at the end of the list.
    merge_lists(devices_old, devices_new)  # Hoping the titles don't change.
    merge_lists(firmwares_old, firmwares_new, "firmware_id")
    pak_infos = await asyncio.gather(*[firmware_info_safe(fw["url"]) for fw in firmwares_old[old_len:]])
    firmwares_old[old_len:] = add_and_clean(pak_infos, firmwares_old[old_len:], "live")
    with open(FILE_DEVICES, 'w', encoding="utf8") as f:
        json.dump(devices_old, f, indent=2)
    with open(FILE_FW_LIVE, 'w', encoding="utf8") as f:
        json.dump(firmwares_old, f, indent=2, default=str)
    return pak_infos


async def add_firmware_manually(args: Namespace) -> None:
    """If a new device/hw ver is involved, it must be added manually first."""
    with open(FILE_FW_MANL, 'r', encoding="utf8") as f:
        firmwares: list[dict[str, Any]] = json.load(f)
    pak_infos = await firmware_info(args.url)
    new = {"url": args.url, "beta": args.beta, "user_hosted_only": args.user_hosted_only}
    if args.source:
        new["source_urls"] = args.source
    if args.note:
        new["note"] = args.note
    firmwares.extend(add_and_clean([pak_infos], [new], "manual"))
    with open(FILE_FW_MANL, 'w', encoding="utf8") as f:
        json.dump(firmwares, f, indent=2)


def write_readme() -> None:
    with open("readme_header.md", 'r', encoding="utf8") as f:
        header = f.read()
    body = make_readme(load_firmwares())
    with open("README.md", 'w', encoding="utf8") as f:
        f.write(header + '\n' + body)


if __name__ == "__main__":
    from contextlib import redirect_stdout
    from io import StringIO

    def add(args: Namespace) -> None:
        asyncio.run(add_firmware_manually(args))
        write_readme()

    def update(args: Namespace) -> None:
        # Catch output from ubireader.
        with redirect_stdout(StringIO()) as f:
            new = asyncio.run(update_live_info())
            write_readme()
        if not args.github:
            print(f.getvalue(), end='')
        print(json.dumps(new or None))  # Empty array is not falsy in JavaScript.

    def readme(args: Namespace) -> None:
        write_readme()

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(required=True, title="commands")
    parser_a = subparsers.add_parser("add", help="add a firmware manually", description="If you want to add a changelog, edit the JSON directly after running this command.")
    parser_a.add_argument("url", help="download link to the firmware")
    parser_a.add_argument("-s", "--source", nargs='*', help="page(s) where the file comes from")
    parser_a.add_argument("-n", "--note")
    parser_a.add_argument("-b", "--beta", action="store_true", help="flag for beta firmwares")
    parser_a.add_argument("-u", "--user-hosted-only", action="store_true", help="flag for firmwares that have only been shared by users")
    parser_a.set_defaults(func=add)
    parser_u = subparsers.add_parser("update", help="get new firmwares from Reolink and update all files")
    parser_u.add_argument("-g", "--github", action="store_true", help="flag for GitHub Actions")
    parser_u.set_defaults(func=update)
    parser_r = subparsers.add_parser("readme", help="generate readme from current files")
    parser_r.set_defaults(func=readme)

    args = parser.parse_args()
    args.func(args)
