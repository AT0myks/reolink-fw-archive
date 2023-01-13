import argparse
import json

from common import load_devices, match


def get_names(devices, model_id, hw_ver_id):
    for device in devices:
        if device["id"] == model_id:
            for hw_ver in device["hardwareVersions"]:
                if hw_ver["id"] == hw_ver_id:
                    return device["title"], hw_ver["title"]
    return None, None


def make_new_firmwares(pak_infos):
    new = []
    devices = load_devices()
    for infos in pak_infos:
        for info in infos:
            if "error" in info:
                continue
            model_id, hw_ver_id = match(info)
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
