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
        self.btn_clear.clicked.connect(self.clear)
        self.btn_sqrt.clicked.connect(self.calculate_sqrt)
        self.btn_fact.clicked.connect(self.calculate_fact)
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
        self.first_num = ''

    def clear(self):
        self.expression = ''
        self.first_num = ''
        self.table.display(0)

    def add_digit(self, digit):
        if digit == '.' and (not self.expression or self.expression[-1] in '+*/**'):
            self.expression += '0' + digit
        elif digit == '.' and '.' in self.expression.split()[-1]:
            return
        else:
            self.expression += digit
        self.table.display(self.expression)

    def add_operator(self, operator):
        if self.expression and self.expression[-1] not in '+*/**':
            self.expression += operator
        elif operator == '-':
            self.expression += operator
        self.first_num = self.expression
        self.expression = ''

    def calculate_sqrt(self):
        try:
            self.table.display((math.sqrt(float(self.expression))))
            self.expression = str((math.sqrt(float(self.expression))))
        except Exception:
                self.table.display('Error')
                self.expression = ''

    def calculate_fact(self):
        try:
            self.table.display((math.factorial(float(self.expression))))
            self.expression = str((math.factorial(float(self.expression))))
        except Exception:
            self.table.display('Error')
            self.expression = ''

    

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
