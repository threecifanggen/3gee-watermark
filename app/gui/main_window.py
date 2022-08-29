"""主界面
"""
import os
from PySide6 import QtWidgets, QtGui
import sys

from .add_tool import AddTool
from .decipher_tool import DecipherTool


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("3GEE水印工具")
        self.setMenuBar()
        self.loadAddTool()

    def setMenuBar(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("&工具")

        add_tool_button = QtGui.QAction("添加水印", self)
        add_tool_button.triggered.connect(self.loadAddTool)
        decipher_tool_button = QtGui.QAction("解码水印", self)
        decipher_tool_button.triggered.connect(self.loadDecipherTool)

        file_menu.addAction(add_tool_button)
        file_menu.addSeparator()
        file_menu.addAction(decipher_tool_button)

        infoMenu = menu.addMenu("&About")

        
        

    def loadAddTool(self):
        self.setCentralWidget(AddTool())

    def loadDecipherTool(self):
        self.setCentralWidget(DecipherTool())