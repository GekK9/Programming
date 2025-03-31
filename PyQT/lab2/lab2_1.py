import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        for button in self.buttonGroup_digits.buttons():
            button.clicked.connect(lambda: self.add_digit(self.sender().text()))
        
        for button in self.buttonGroup_binary.buttons():
            button.clicked.connect(lambda: self.add_operator(self.sender().text()))
        self.btn_eq.clicked.connect(self.result)
        self.expression = ''
        self.first_num = ''
        
    def result(self):
        if "^" in self.first_num and not self.first_num == '':
            self.first_num = self.first_num.replace('^', '**')
            self.table.display(float(eval(self.first_num + self.expression)))
        else:
            self.first_num == '0'
            self.table.display(float(eval(self.first_num + self.expression)))
        self.expression = str(eval(self.first_num + self.expression))
        print(float(self.expression))    
        self.first_num = ''

    def add_digit(self, digit):
        if digit == '.' and (not self.expression or self.expression[-1] in '+-*/**'):
            self.expression += '0' + digit
        elif digit == '.' and '.' in self.expression.split()[-1]:
            return
        else:
            self.expression += digit
        self.table.display(self.expression)

    def add_operator(self, operator):
        if self.expression and self.expression[-1] not in '+-*/**':
            self.expression += operator
        self.first_num = self.expression
        self.expression = ''

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
