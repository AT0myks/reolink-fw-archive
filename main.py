#!/usr/bin/env python3

import asyncio
import json
import random
import re
from datetime import date, datetime
from zoneinfo import ZoneInfo

import aiohttp
from dateutil.parser import parse as dtparse
from lxml.html import document_fromstring, fragment_fromstring, tostring
from lxml.html.builder import OL, LI
from reolinkfw import get_info
from waybackpy import WaybackMachineCDXServerAPI

WAYBACK_MAX_CONN = 20


async def get_one(session, url, type_):
    async with session.get(url) as resp:
        return await (resp.json() if type_ == "json" else resp.text())


async def get_all(urls, type_, limit_per_host=0):
    conn = aiohttp.TCPConnector(limit_per_host=limit_per_host)
    async with aiohttp.ClientSession(connector=conn) as session:
        return await asyncio.gather(*[get_one(session, url, type_) for url in urls])


def md_link(label, url):
    return f"[{label}]({url})"


def make_changes(changes):
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


def make_readme(firmwares):
    text = ''
    models = sorted(set(fw["model"] for fw in firmwares))
    for model in models:
        text += "<details>\n  <summary>" + model + "</summary>\n"
        model_fw = [fw for fw in firmwares if fw["model"] == model]
        hw_vers = sorted(set(fw["hw_ver"] for fw in model_fw))
        for hv in hw_vers:
            text += "\n  ### " + hv + "\n"
            text += "Version | Date | Changes | Notes\n"
            text += "--- | --- | --- | ---\n"
            for fw in (f for f in model_fw if f["hw_ver"] == hv): #sort by date
                if "filename" in fw:
                    dl_url = fw["url"] + '?download_name=' + fw["filename"]
                else:
                    dl_url = fw["url"]
                version = md_link(fw["version"], dl_url)
                if isinstance(fw["display_time"], str):
                    dt = datetime.fromisoformat(fw["display_time"]).date()
                else:
                    dt = fw["display_time"].date()
                date_str = str(dt).replace('-', chr(0x2011))
                if "changelog" in fw:
                    new = make_changes(fw["changelog"]) if len(fw["changelog"]) > 1 else fw["changelog"][0]
                else:
                    new = ''
                notes = fw.get("note", '').replace("\n", '')
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
    return re.split("\s*</?[pP]>\s*<[pP]>|\s*<br />\s*", text)


def parse_timestamps(display_time, updated_at):
    """For v3."""
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
    cdx = WaybackMachineCDXServerAPI("https://reolink.com/firmware", filters=["statuscode:200"])
    snapshots = (snap.archive_url for snap in cdx.snapshots())  # set()?
    links = []
    for response in await get_all(snapshots, "text", limit_per_host):
        doc = document_fromstring(response)
        for a in doc.iter("a"):
            href = a.get("href")
            if href is not None and ".zip" in href:
                link = "http" + href.split("http")[-1]
                if link not in links:  # Keep order, don't use set.
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
    html = await get_one(session, url, "text")
    doc = document_fromstring(html)
    main = doc.find("./body/main")
    firmwares = []
    title = doc.find("./head/title").text
    # Could also use date in link or in firmware.
    dt = dtparse(title.split("Firmware")[0]).date()
    for body in main.find_class("article-body"):
        if new := parse_old_support_page_changes(body.text_content()):
            break
    for table in main.findall(".//table"):
        for tr in table.iter("tr"):
            if len(tr) == 3:
                model, firmware, hardware = tr
            elif len(tr) == 4:
                model, firmware, _, hardware = tr
            elif len(tr) == 2:
                model, firmware = tr
                hardware = None
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


async def get_firmwares_from_archives_v1(limit_per_host=WAYBACK_MAX_CONN):
    urls = await get_archives_v1_firmware_links(limit_per_host)
    return await asyncio.gather(*[get_info(url) for url in urls])


def merge_devices(live, old):
    """Modify live in-place and return it."""
    for olddev in old:
        if olddev["id"] >= 10**5:
            live.append(olddev)
        else:
            for livedev in live:
                if livedev["id"] == olddev["id"]:
                    livedev["hardwareVersions"].extend(olddev["hardwareVersions"])
                    break
    return live


def parse_build_date(build_date):
    return date(2000 + int(build_date[:2]), int(build_date[2:4]), int(build_date[4:]))


def clean_model(model):
    return model.removesuffix("-5MP").removesuffix(" (NVR)").lower()


def clean_hw_ver(hw_ver):
    return hw_ver.replace('-', '_').strip()


def get_model_id(devices, model):
    for dev in devices:
        if clean_model(dev["title"]) == clean_model(model):
            return dev["id"]
    return None


def get_hw_ver_id(devices, model_id, hw_ver_names):
    for dev in devices:
        if dev["id"] == model_id:
            for hw_ver in dev["hardwareVersions"]:
                for name in hw_ver["title"].split(" or "):
                    clean = clean_hw_ver(name)
                    if any(clean == clean_hw_ver(name) for name in hw_ver_names):
                        return hw_ver["id"]
    return None


# def get_hw_ver_name(devices, model_id, hw_ver_id):
#     for dev in devices:
#         if dev["id"] == model_id:
#             for hw_ver in dev["hardwareVersions"]:
#                 if hw_ver_id == hw_ver["id"]:
#                     return hw_ver["title"]
#     return None


def random_firmware_id():
    return random.randrange(10**6, 10**7)


def longest_string(*strings):
    res = ''
    for s in set(strings):
        if len(s) > len(res):
            res = s
    return res


def match_and_correct(firmware, devices):
    """Modifies firmware in-place. get_info must have been called."""
    if firmware.get("firmware_id") is None:
        firmware["firmware_id"] = random_firmware_id()
    if firmware.get("model_id") is None:
        dti = firmware["display_type_info"]
        # names = set((dti, firmware.get("model", dti)))
        name = longest_string(*dti.split('/'), *firmware.get("model", dti).split('/'))
        firmware["model_id"] = get_model_id(devices, name)
    model_id = firmware["model_id"]
    if firmware.get("hw_ver_id") is None:
        keys = ("board_type", "detail_machine_type", "board_name", "hw_ver")
        hw_names = set(firmware.get(key) for key in keys if firmware.get(key))
        firmware["hw_ver_id"] = get_hw_ver_id(devices, model_id, hw_names)
    if firmware.get("display_time") is None:
        firmware["display_time"] = parse_build_date(firmware["build_date"])
    # if firmware.get("hw_ver") is None:
    #     firmware["hw_ver"] = get_hw_ver_name(devices, model_id, firmware["hw_ver_id"])
    if 'v' not in firmware.get("version", '').lower():
        prefix = firmware["firmware_version_prefix"]
        firmware["version"] = prefix + '.' + firmware["version_file"]


def keep_most_recent(firmwares):
    """Return a list containing only the most recent snapshot for each unique firmware file link."""
    urls = {fw["url"] for fw in firmwares}
    return [sorted((fw for fw in firmwares if fw["url"] == url), key=lambda fw: fw["archive_url"])[-1] for url in urls]


async def generate_support_archives_firmwares(limit_per_host=WAYBACK_MAX_CONN):
    firmwares = await from_support_archives(limit_per_host=limit_per_host)
    filtered = keep_most_recent(firmwares)
    with (open("devices_live.json", 'r', encoding="utf8") as live,
            open("devices_old.json", 'r', encoding="utf8") as old):
        devices = merge_devices(json.load(live), json.load(old))
    info =  await asyncio.gather(*[get_info(fw["url"]) for fw in filtered])
    with_info = [{**a, **b} for a, b in zip(filtered, info)]
    for f in with_info:
        if "error" not in f:
            match_and_correct(f, devices)
    with open("firmwares_old_support.json", 'w', encoding="utf8") as f:
        json.dump(with_info, f, indent=2, default=str)
