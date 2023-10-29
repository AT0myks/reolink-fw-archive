import json

FILE_DEVICES = "devices.json"


def load_devices():
    with open(FILE_DEVICES, 'r', encoding="utf8") as f:
        return json.load(f)


def get_item_index(items, key, value):
    """Return the index of the first item in items that has this value for this key.
    
    The key must exist in each item. Return None if no match is found.
    """
    for idx, item in enumerate(items):
        if item[key] == value:
            return idx
    return None


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


def get_names(devices, model_id, hw_ver_id):
    for device in devices:
        if device["id"] == model_id:
            for hw_ver in device["hardwareVersions"]:
                if hw_ver["id"] == hw_ver_id:
                    return device["title"], hw_ver["title"]
    return None, None
