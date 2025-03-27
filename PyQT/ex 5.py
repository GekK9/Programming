from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 300, 360)
        self.setWindowTitle('Order')

        self.main_layout = QHBoxLayout(self)
        self.order_box = QHBoxLayout()
        self.check_boxes = QVBoxLayout()
        self.names = QVBoxLayout()

        self.cheque_box_widget = QWidget()
        self.cheque_box_layout = QVBoxLayout(self.cheque_box_widget) 


        self.main_layout.addLayout(self.order_box)
        self.main_layout.addWidget(self.cheque_box_widget)
        self.order_box.addLayout(self.check_boxes)
        self.order_box.addLayout(self.names)
        self.main_layout.addStretch()
        self.cheque_box_layout.minimumHeightForWidth(400)



        self.goods = [
            'Чизбургер', 'Гамбургер', 'Кока-кола', 'Нагеттсы',
            'Картошка Фри', 'Вода', 'Котлета',
        ]
        self.order_box.addStretch()
        self.input_boxes = {
            
        }
        
        for item in self.goods:
            
            self.check_box = QCheckBox(f"{item}", self)
            self.check_box.stateChanged.connect(self.count)
            self.check_box.stateChanged.connect(self.order)
            self.check_boxes.addWidget(self.check_box)

            input_box = QLineEdit("0", self)
            input_box.setFixedSize(30, 17)
            input_box.setDisabled(True)
            self.names.addWidget(input_box)
            self.input_boxes[self.check_box] = input_box
            

        self.check_boxes.setSpacing(15)
        self.names.setSpacing(15)
        
        self.names.addStretch()

        self.btn = QPushButton('Заказать')
        self.btn.clicked.connect(self.order)

        self.check_boxes.addWidget(self.btn)
        
        self.check_boxes.addWidget(self.btn)
        self.check_boxes.addStretch()

        self.text = QLabel(self)
        self.text.setText('Ваш заказ:')
        self.goods = QLabel(self)
        self.cheque_box_layout.addWidget(self.text)
        self.cheque_box_layout.addWidget(self.goods)
        self.goods.setStyleSheet("border: 0px")
        self.text.setStyleSheet("border: 0px")
        self.text.hide()
        
    def order(self):
        self.cheque_box_widget.setStyleSheet("border: 2px solid grey; padding: 10px;") 
        self.text.show()
        self.goods.setText('')

        for check_box, input_box in self.input_boxes.items():
            if check_box.isChecked():
                self.goods.setText(f"{check_box.text()}")
                print(check_box.text())
            else:
                print('0')

        
        
        
    def count(self):
        for check_box, input_box in self.input_boxes.items():
            if check_box.isChecked():
                input_box.setDisabled(False)
                input_box.setText("1")
            else:
                input_box.setDisabled(True)
                input_box.setText("0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())