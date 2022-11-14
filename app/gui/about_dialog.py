from PySide6 import QtWidgets

from ..core import VERSION

class AboutDialog(QtWidgets.QDialog):
    """「关于本软件」
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关于本软件")
        self.setFixedSize(200, 200)
        label = QtWidgets.QLabel(f"版本号：v{VERSION}。\n本软件由3GEE开发。", self)
        label.setMargin(30)