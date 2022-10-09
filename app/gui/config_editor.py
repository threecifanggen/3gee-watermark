"""配置编辑器
"""
from PySide6 import QtWidgets, QtGui
from .config_list import ConfigList
class ConfigEditor(QtWidgets.QDialog):
    
    def __init__(
        self,
        connect_config_list: ConfigList,
        config_name: None | str = None):
        super().__init__()
        if config_name is None:
            pass
        pass