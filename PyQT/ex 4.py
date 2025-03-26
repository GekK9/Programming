from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('CheckBoxes')

        for i in range(4):
            check_box = QCheckBox(f"edit{i+1}", self)
            check_box.move(10, (i * 30) + 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())