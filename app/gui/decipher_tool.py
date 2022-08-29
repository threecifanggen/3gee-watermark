"""解码水印工具
"""
from PySide6 import QtWidgets, QtGui

import os

class DecipherTool(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initInputFileDir = os.path.expanduser("~")
        self.fileDirButton = QtWidgets.QPushButton("选择文件")
        self.decipherButton = QtWidgets.QPushButton("解码")
        
        
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.decipherButton, 0, 0, 1, 2)
        # self.layout.addWidget(self.encripherButton, 0, 2, 1, 2)
        self.layout.addWidget(self.fileDirButton, 1, 0, 1, 4)
    

        self.inputFileDirs = []

        self.fileDirButton.clicked.connect(self.msg)
        self.show()

    def msg(self, _):
        directory, _ = QtWidgets.QFileDialog.getOpenFileNames(self,  "选择图片文件", self.initInputFileDir, "All Files (*);;JPG Files (*.jpg)")
        self.inputFileDirs = directory
        print(self.inputFileDirs)
