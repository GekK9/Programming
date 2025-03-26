from PyQt5.QtWidgets import QApplication, QWidget
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 395, 120)
        self.setWindowTitle('XXX')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())