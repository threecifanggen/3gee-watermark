import os
from PySide6 import QtWidgets, QtGui
import sys


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("3GEE水印工具")

        self.initInputFileDir = os.path.expanduser("~")
        self.fileDirButton = QtWidgets.QPushButton("选择文件")
        self.fileNameList = QtWidgets.QLabel("ss")


        self.decipherButton
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.fileDirButton, 0, 0, 1, 4)
    
        

        self.inputFileDirs = []

        self.fileDirButton.clicked.connect(self.msg)
        self.show()

    def msg(self, _):
        directory, _ = QtWidgets.QFileDialog.getOpenFileNames(self,  "选择图片文件", self.initInputFileDir, "All Files (*);;JPG Files (*.jpg)")
        self.inputFileDirs = directory
        print(self.inputFileDirs)
        self.fileDirNames.setText(self.inpu)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('hand.ico'))
    w = MainWindow()
    w.resize(360, 360)
    w.show()
    app.exec()
