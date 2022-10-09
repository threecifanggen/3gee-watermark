from msilib import Table
from tomlkit import *

def edit_config(config_doc, config_name, check_str, password_img, password_wm):
    config_single = table(config_name)
    config_single.add("check_str", check_str)
    config_single.add("password_img", password_img)
    config_single.add("password_wm", password_wm)
    config_doc['config_name'] = config_single
    return config_doc


def remove_config(config_doc, config_name):
    config_doc.pop(config_name)

def write_config(config_doc, dir):
    """写配置
    """
    config_str = dumps(config_doc)
    with open(dir, "w", encoding="utf8") as f:
        f.write(config_str)
    