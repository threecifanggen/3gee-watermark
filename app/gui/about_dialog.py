from PySide6 import QtWidgets

from ..core import VERSION

class AboutDialog(QtWidgets.QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关于本软件")
        self.setFixedSize(200, 200)