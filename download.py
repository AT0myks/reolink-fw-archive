#!/usr/bin/env python3

import argparse
import asyncio
import hashlib
import logging
from functools import partial
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZipFile, is_zipfile

import aiohttp

__version__ = "1.1.0"

_LOGGER = logging.getLogger()

PAK_EXT = ".pak"
ZIP_EXT = ".zip"
TMP_EXT = ".pakorzip"

PAK_MAGIC = b"\x13Yr2"

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
            or urlpath.endswith(ZIP_EXT) or url.endswith(ZIP_EXT) or filename.endswith(ZIP_EXT)):
        return ZIP_EXT
    elif (response.content_type in ("application/x-pak",) or urlpath.endswith(PAK_EXT)
            or url.endswith(PAK_EXT) or filename.endswith(PAK_EXT)):
        return PAK_EXT
    return None


def is_pakfile(file):
    if hasattr(file, "read"):
        magic = file.read(4)
        file.seek(0)
        return magic == PAK_MAGIC
    try:
        with open(file, "rb") as f:
            return f.read(4) == PAK_MAGIC
    except OSError:
        return False


async def _download(sessions, url, path: Path):
    session = sessions[1] if urlparse(url).netloc == "drive.google.com" else sessions[0]
    async with session.get(url) as resp:
        if not resp.ok:
            _LOGGER.log(1, f"Error {resp.status}: {url}")
            return False
        if (ext := find_extension(resp)) is not None:
            path = path.with_suffix(ext)
        elif resp.content_type != "text/html":
            _LOGGER.log(1, f"Warning: could not find file type for {url}")
        else:
            return False
        _LOGGER.log(1, f"Downloading {url} to {path}")
        with open(path, "wb") as f:
            async for chunk in resp.content.iter_chunked(2**16):
                f.write(chunk)
    if path.suffix == TMP_EXT:
        if is_zipfile(path):
            path.rename(path.with_suffix(ZIP_EXT))
        elif is_pakfile(path):
            path.rename(path.with_suffix(PAK_EXT))
    return True


def calc_sha256(file):
    sha256 = hashlib.sha256()
    if isinstance(file, (str, Path)):
        with open(file, "rb") as f:
            for block in iter(partial(f.read, 1024**2), b''):
                sha256.update(block)
    elif hasattr(file, "read"):
        for block in iter(partial(file.read, 1024**2), b''):
            sha256.update(block)
    else:
        raise TypeError("file must be a file or file-like object")
    return sha256.hexdigest()


def already_downloaded(path: Path, sha256: str):
    as_pak = path.with_suffix(PAK_EXT)
    as_zip = path.with_suffix(ZIP_EXT)
    if as_pak.is_file():
        return calc_sha256(as_pak) == sha256
    elif is_zipfile(as_zip):
        with ZipFile(as_zip) as myzip:
            for name in myzip.namelist():
                with myzip.open(name) as file:
                    if is_pakfile(file) and calc_sha256(file) == sha256:
                        return True
    return False


async def download(sessions, devices, sha256: str, info, directory: Path, force=False):
    model, hw_ver = get_names(devices, info["model_id"], info["hw_ver_id"])
    version = info["info"]["firmware_version_prefix"] + '.' + info["info"]["version_file"]
    filename = "__".join((model, hw_ver, version))
    path = directory / model / hw_ver.strip() / (filename + TMP_EXT)
    if not force and (await asyncio.to_thread(already_downloaded, path, sha256)):
        _LOGGER.log(2, f"Already exists (sha256): {path.stem}")
        return True, None, None
    path.parent.mkdir(parents=True, exist_ok=True)
    exception = None
    # Prioritize original Reolink URLs.
    for url in sorted(info["download"], key=is_original_url, reverse=True):
        try:
            if await _download(sessions, url, path):
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
    parser.add_argument("-f", "--force", action="store_true", help="download even if file exists (overwrite)")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase verbosity. Can appear multiple times")
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    def filter(verbosity, record):
        return record.levelno - 1 <= verbosity

    _LOGGER.setLevel(0)
    _LOGGER.addFilter(partial(filter, args.verbose))
    sh = logging.StreamHandler()
    sh.setLevel(0)
    sh.setFormatter(logging.Formatter("%(message)s"))
    _LOGGER.addHandler(sh)

    count = 0

    async def print_progress(target):
        while count != target:
            print(f"{count}/{target}", end='\r')
            await asyncio.sleep(.1)

    def callback(fut):
        nonlocal count
        count += 1

    conn = aiohttp.TCPConnector(limit=args.max_connections)
    conn_drive = aiohttp.TCPConnector(limit=args.max_connections_gdrive)
    async with (aiohttp.ClientSession(connector=conn) as session,
                aiohttp.ClientSession(connector=conn_drive) as session_drive):
        pak_info = await fetch(session, "https://raw.githubusercontent.com/AT0myks/reolink-fw-archive/main/pak_info.json")
        devices = await fetch(session, "https://raw.githubusercontent.com/AT0myks/reolink-fw-archive/main/devices.json")
        sessions = [session, session_drive]
        tasks = [asyncio.create_task(download(sessions, devices, sha256, info, args.directory, args.force)) for sha256, info in pak_info.items()]
        for task in tasks:
            task.add_done_callback(callback)
        print(f"Downloading {len(tasks)} firmwares")
        if args.verbose == 0:
            asyncio.create_task(print_progress(len(tasks)))
        results = await asyncio.gather(*tasks)
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
