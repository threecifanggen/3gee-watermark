"""加水印工具
"""
from PySide6 import QtWidgets, QtGui

import os

from .config_list import ConfigList
from ..core.watermark import encriptor_str
from .config_editor import ConfigEditor

class AddTool(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initInputFileDir = os.path.expanduser("~")
        self.fileDirButton = QtWidgets.QPushButton("选择文件")
        self.encriptorButton = QtWidgets.QPushButton("加水印")
        self.addConfButton = QtWidgets.QPushButton("添加配置")
        self.ConfigList = ConfigList()        
        
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.encriptorButton, 0, 2, 1, 2)
        self.layout.addWidget(self.fileDirButton, 1, 3, 1, 4)


        self.layout.addWidget(self.ConfigList, 0, 0, 4, 2)
        self.layout.addWidget(self.addConfButton, 5, 0, 1, 2)
    

        self.inputFileDirs = []

        self.fileDirButton.clicked.connect(self.msg)
        self.addConfButton.clicked.connect(self.add_config)
        self.show()

    def msg(self, _):
        directory, _ = QtWidgets.QFileDialog.getOpenFileNames(self,  "选择图片文件", self.initInputFileDir, "All Files (*);;JPG Files (*.jpg)")
        self.inputFileDirs = directory
        print(self.inputFileDirs)

    def add_config(self):
        self.config_editor = ConfigEditor(self.ConfigList, None)
        self.config_editor.show()
