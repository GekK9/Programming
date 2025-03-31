import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lab2_2.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())