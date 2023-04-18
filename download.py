#!/usr/bin/env python3

import argparse
import asyncio
import logging
from functools import partial
from pathlib import Path
from urllib.parse import urlparse

import aiohttp

__version__ = "1.0.1"

_LOGGER = logging.getLogger()

REOLINK_DOMAINS = (
    "support.reolink.com",
    "support-d.reolink.com",
    "cdn.reolink.com",
    "reolink.zendesk.com",
    "home-cdn.reolink.us",
    "reolink-storage.s3.amazonaws.com"
)


# Copied from release.py so that there's only this file to download.
def get_names(devices, model_id, hw_ver_id):
    for device in devices:
        if device["id"] == model_id:
            for hw_ver in device["hardwareVersions"]:
                if hw_ver["id"] == hw_ver_id:
                    return device["title"], hw_ver["title"]
    return None, None


def is_original_url(url):
    # Google Drive links given by Reolink obviously cannot be 'detected'.
    netloc = urlparse(url).netloc
    return netloc in REOLINK_DOMAINS or url.startswith("https://s3.amazonaws.com/reolink-storage")


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json(content_type=None)


def find_extension(response):
    url = str(response.url)
    urlpath = urlparse(url).path
    if response.content_disposition is not None:
        filename = response.content_disposition.filename or ''
    else:
        filename = ''
    if (response.content_type in ("application/zip", "application/x-zip-compressed")
            or urlpath.endswith(".zip") or url.endswith(".zip") or filename.endswith(".zip")):
        return ".zip"
    elif (response.content_type in ("application/x-pak",) or urlpath.endswith(".pak")
            or url.endswith(".pak") or filename.endswith(".pak")):
        return ".pak"
    return None


async def _download(sessions, url, path, force=False):
    session = sessions[1] if urlparse(url).netloc == "drive.google.com" else sessions[0]
    async with session.get(url) as resp:
        if not resp.ok:
            _LOGGER.log(1, f"Error {resp.status}: {url}")
            return False
        if (ext := find_extension(resp)) is not None:
            path = path.with_name(path.name + ext)
        elif resp.content_type != "text/html":
            _LOGGER.log(1, f"Warning: could not find file type for {url}")
            path = path.with_name(path.name + ".pakorzip")
        else:
            return False
        if not force and path.is_file() and int(resp.headers.get("content-length", -1)) == path.stat().st_size:
            _LOGGER.log(2, f"Already exists: {path.name}")
            return True
        _LOGGER.log(1, f"Downloading {url} to {path}")
        with open(path, "wb") as f:
            async for chunk in resp.content.iter_chunked(1024):
                f.write(chunk)
    return True


async def download(sessions, devices, info, directory, force=False):
    model, hw_ver = get_names(devices, info["model_id"], info["hw_ver_id"])
    version = info["info"]["firmware_version_prefix"] + '.' + info["info"]["version_file"]
    filename = "__".join((model, hw_ver, version))
    path = directory / model / hw_ver.strip() / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    exception = None
    # Prioritize original Reolink URLs.
    for url in sorted(info["download"], key=is_original_url, reverse=True):
        try:
            if await _download(sessions, url, path, force):
                return True, url, None
        except Exception as e:
            exception = e
        else:
            exception = None
    return False, url, exception


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=Path, default=Path.cwd() / "reolink-archive", help="directory where the files will be downloaded. Default: in a new dir created in the current one")
    parser.add_argument("-g", "--max-connections-gdrive", type=int, default=1, help="max simultaneous downloads for Google Drive links. Default: %(default)s")
    parser.add_argument("-m", "--max-connections", type=int, default=20, help="max simultaneous downloads for other links. Default: %(default)s")
    parser.add_argument("-f", "--force", action="store_true", help="download even if file exists")
    parser.add_argument("--verbose", "-v", action="count", default=0, help="increase verbosity. Can appear multiple times")
    args = parser.parse_args()

    def filter(verbosity, record):
        return record.levelno - 1 <= verbosity

    _LOGGER.setLevel(0)
    _LOGGER.addFilter(partial(filter, args.verbose))
    sh = logging.StreamHandler()
    sh.setLevel(0)
    sh.setFormatter(logging.Formatter("%(message)s"))
    _LOGGER.addHandler(sh)

    conn = aiohttp.TCPConnector(limit=args.max_connections)
    conn_drive = aiohttp.TCPConnector(limit=args.max_connections_gdrive)
    async with (aiohttp.ClientSession(connector=conn) as session,
            aiohttp.ClientSession(connector=conn_drive) as session_drive):
        pak_info = await fetch(session, "https://raw.githubusercontent.com/AT0myks/reolink-fw-archive/main/pak_info.json")
        devices = await fetch(session, "https://raw.githubusercontent.com/AT0myks/reolink-fw-archive/main/devices.json")
        sessions = [session, session_drive]
        coros = [download(sessions, devices, info, args.directory, args.force) for info in pak_info.values()]
        print(f"Downloading {len(coros)} firmwares")
        results = await asyncio.gather(*coros)
    successes = failures = 0
    for success, url, exception in results:
        if exception is not None:
            print(repr(exception), url)
        if success:
            successes += 1
        else:
            failures += 1
    print(successes, "successful")
    print(failures, "failures")


if __name__ == "__main__":
    asyncio.run(main())