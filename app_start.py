import sys

from PySide6 import QtWidgets
from app.gui import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QtGui.QIcon('hand.ico'))
    w = MainWindow()
    w.setFixedSize(360, 200)
    w.show()
    app.exec()