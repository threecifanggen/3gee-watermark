"""配置列表
"""
from PySide6 import QtWidgets
import os
from tomlkit import parse
from tomlkit.toml_document import TOMLDocument

from ..core.config_edit import (
    edit_config,
    remove_config,
    write_config
)

class ConfigList(QtWidgets.QListWidget):

    config_list_file:  TOMLDocument # 配置文件
    config_file: str # 配置文件地址 

    def __init__(self):

        super().__init__()
        self.showConfigList()

    
    def showConfigList(self):
        """展示配置列表
        """
        app_data = os.getenv("APPDATA")

        # 查看是否存在配置文件夹
        config_dir = os.path.join(app_data, "3geeWater")
        if not os.path.isdir(config_dir):
            os.mkdir(config_dir)

        # 查看是否存在配置文件
        config_file = os.path.join(config_dir, "config_list.toml")
        self.config_file = config_file
        if not os.path.exists(config_file):
             with open(config_file, 'a+'): pass
        
        # 读取配置文件
        self.config_list_file = parse(open(config_file, encoding="utf8").read())

        # 展示配置列表
        for config_name in self.config_list_file.keys():
            config = QtWidgets.QListWidgetItem(config_name, self)
    
    def write_config(self, config_name, check_str, password_img, password_wm):
        self.config_list_file = edit_config(
            self.config_list_file,
            config_name,
            check_str,
            password_img,
            password_wm)
        write_config(self.config_list_file, self.config_file)
        self.showConfigList()

