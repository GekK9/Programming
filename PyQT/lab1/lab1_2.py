from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QErrorMessage
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('Миникалькулятор')
        
        # labels and text boxes
        self.FirstNum_label = QLabel(self)
        self.FirstNum_label.setText("Первое число(целое):")
        self.FirstNum_label.move(20, 20)

        self.FirstNum_textBox = QLineEdit(self)
        self.FirstNum_textBox.move(20, 40)

        self.SecondNum_label = QLabel(self)
        self.SecondNum_label.setText("Второе число(целое):")
        self.SecondNum_label.move(20, 90)

        self.SecondNum_textBox = QLineEdit(self)
        self.SecondNum_textBox.move(20, 110)

        self.Sum_label = QLabel(self)
        self.Sum_label.setText("Сумма:")
        self.Sum_label.move(325, 25)

        self.Sub_label = QLabel(self)
        self.Sub_label.setText("Разность:")
        self.Sub_label.move(325, 55)

        self.Mult_label = QLabel(self)
        self.Mult_label.setText("Произведение:")
        self.Mult_label.move(325, 85)

        self.Div_label = QLabel(self)
        self.Div_label.setText("Частное:")
        self.Div_label.move(325, 115)

        # numBoxes
        self.LCD_sum = QLCDNumber(self)
        self.LCD_sum.move(410, 20)   

        self.LCD_sub = QLCDNumber(self)
        self.LCD_sub.move(410, 50) 

        self.LCD_mult = QLCDNumber(self)
        self.LCD_mult.move(410, 80) 

        self.LCD_div = QLCDNumber(self)
        self.LCD_div.move(410, 110)        
        
        # button
        self.btn = QPushButton('->', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 70)
        self.btn.clicked.connect(self.Calculation)

    def Calculation(self):

        self.sum = 0
        self.sub = 0
        self.mult = 0
        self.div = 0

        self.sum = (f"{float(self.FirstNum_textBox.text()) + float(self.SecondNum_textBox.text())}")
        self.sub = (f"{float(self.FirstNum_textBox.text()) - float(self.SecondNum_textBox.text())}")
        self.mult = (f"{float(self.FirstNum_textBox.text()) * float(self.SecondNum_textBox.text())}")

        if self.SecondNum_textBox.text() == '0':
            self.div = 'Error'
            self.Error = QErrorMessage()
            self.Error.showMessage("Деление на ноль!")
            
        else: 
            self.div = (f"{float(self.FirstNum_textBox.text()) / float(self.SecondNum_textBox.text())}")

        self.LCD_sum.display(self.sum)
        self.LCD_sub.display(self.sub)
        self.LCD_mult.display(self.mult)
        self.LCD_div.display(self.div)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())


