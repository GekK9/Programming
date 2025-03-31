from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QLineEdit
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 200, 120)
        self.setWindowTitle('CheckBoxes')

        self.input_boxes = {}

        for i in range(4):
            check_box = QCheckBox(f"edit{i + 1}", self)
            check_box.move(10, 15 + (i * 25))
            check_box.stateChanged.connect(self.show_and_hide)

            input_box = QLineEdit(f"Поле edit{i + 1}", self)
            input_box.move(70, (i* 25) + 13)
            input_box.resize(100, 20)

            self.input_boxes[check_box] = input_box

            input_box.hide()
            
    def show_and_hide(self):
        for check_box, input_box in self.input_boxes.items():
            if check_box.isChecked():
                input_box.show()
            else:
                input_box.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())