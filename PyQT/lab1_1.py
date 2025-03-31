from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 500)
        self. setWindowTitle('I')
#Lines for text
        self.first_line = QLineEdit(self)
        self.first_line. move(50, 250)
        self.second_line = QLineEdit(self)
        self.second_line.move(300, 250)
#Button
        self. btn = QPushButton("->", self)
        self.count = 0
        self. btn.resize(self.btn.sizeHint())
        self. btn.move(205, 249)
        self.btn.clicked.connect(self.change_arrow)
        self.btn.clicked.connect(self.swap_text)
#func for btn
    def change_arrow(self):
        self.count += 1
        if self.count % 2 == 1:
            self. btn.setText("<-")
        else:
            self.btn.setText("->")
    def swap_text(self):
        if self.count % 2:
            text = self.first_line.text()
            self.first_line.setText('')
            self.second_line.setText(f"{text}")
        else:
            text = self. second_line.text()
            self.second_line.setText('')
            self.first_line.setText(f"{text}")
if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())