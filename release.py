import argparse
import json
from collections.abc import Iterable, Mapping
from typing import Any

from common import get_names, load_devices, match


def make_new_firmwares(pak_infos: Iterable[Iterable[Mapping[str, Any]]]) -> str:
    new: list[str] = []
    devices = load_devices()
    for infos in pak_infos:
        for info in infos:
            if "error" in info:
                continue
            model_id, hw_ver_id = match(info)
            # Better to print something with Nones than silently
            # ignoring a firmware, so give impossible IDs as default.
            model_id = model_id if model_id is not None else -1
            hw_ver_id = hw_ver_id if hw_ver_id is not None else -1
            model, hw_ver = get_names(devices, model_id, hw_ver_id)
            ver = info["firmware_version_prefix"] + '.' + info["version_file"]
            new.append(f"- New firmware {ver} for {model} ({hw_ver})")
    if len(new) == 1:
        return new[0].removeprefix("- ")
    return '\n'.join(new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json")
    args = parser.parse_args()
    with open("body.md", 'w', encoding="utf8") as f:
        f.write(make_new_firmwares(json.loads(args.json)))
