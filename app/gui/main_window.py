"""主界面
"""
import os
from PySide6 import QtWidgets, QtGui
import sys

from .add_tool import AddTool
from .decipher_tool import DecipherTool
from .about_dialog import AboutDialog


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
        about_button = QtGui.QAction("关于本软件", self)
        about_button.triggered.connect(self.loadAboutDialog)
        infoMenu.addAction(about_button)



    def loadAddTool(self):
        self.setCentralWidget(AddTool())

    def loadDecipherTool(self):
        self.setCentralWidget(DecipherTool())

    def loadAboutDialog(self):
        self.about_dialog = AboutDialog()
        self.about_dialog.show()