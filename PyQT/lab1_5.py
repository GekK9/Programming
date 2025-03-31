from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
import sys

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # параметры окна
        self.setGeometry(300, 300, 300, 360)
        self.setWindowTitle('Order')

        # создаем макеты
        self.main_layout = QVBoxLayout(self)
        self.order_box = QHBoxLayout()
        self.check_boxes = QVBoxLayout()
        self.names = QVBoxLayout()

        self.cheque_box_widget = QWidget()
        self.cheque_box_layout = QVBoxLayout(self.cheque_box_widget)
        self.cheque_box_widget.setStyleSheet("border: 2px solid grey; padding: 10px;")  
        self.cheque_box_widget.hide()

        self.main_layout.addLayout(self.order_box)
        self.main_layout.addWidget(self.cheque_box_widget)
        self.order_box.addLayout(self.check_boxes)
        self.order_box.addLayout(self.names)

        self.main_layout.addStretch()

        self.goods = {
            "100" : 'Чизбургер', "80": 'Гамбургер', "60": 'Кока-кола', "120" : 'Нагеттсы',
            "110": 'Картошка Фри', "40": 'Вода',
        }

        self.order_box.addStretch()

        self.input_boxes = {}
        
        # выводим чекбоксы, их названия и поле для ввода количества    
        for price, name in self.goods.items():
            
            self.check_box = QCheckBox(f"{name}", self)
            self.check_box.stateChanged.connect(self.count)
            self.check_box.stateChanged.connect(self.order)
            self.check_boxes.addWidget(self.check_box)

            input_box = QLineEdit("0", self)
            input_box.setFixedSize(30, 17)
            input_box.setDisabled(True)
            self.names.addWidget(input_box)
            self.input_boxes[self.check_box] = (input_box, price)
            
        self.check_boxes.setSpacing(15)
        self.names.setSpacing(15)
        self.names.addStretch()

        self.btn = QPushButton('Заказать')
        self.btn.clicked.connect(self.order)
        self.check_boxes.addWidget(self.btn)
        self.check_boxes.addStretch()

        self.goods = QLabel(self)
        self.cheque_box_layout.addWidget(self.goods)
        self.goods.setStyleSheet("border: 0px")
        
    def order(self):
        for i in reversed(range(self.cheque_box_layout.count())): 
            widget = self.cheque_box_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
                
        self.text = QLabel('Ваш заказ', self)
        self.text.setText('Ваш заказ:')
        self.text.setStyleSheet("border: 0px")
        self.cheque_box_layout.addWidget(self.text)

        total_price = 0
        has_order = False

        for check_box, (input_box, price) in self.input_boxes.items():
            if check_box.isChecked():
                self.cheque_box_widget.setStyleSheet("border: 2px solid grey; padding: 10px;") 
                quantity = int(input_box.text())
                if quantity > 0:
                    # Добавление информации о выбранном блюде
                    order_info = QLabel(f"{check_box.text()}: {quantity} x {price} руб. = {quantity * int(price)} руб", self)
                    order_info.setStyleSheet("border: 0px")
                    self.cheque_box_layout.addWidget(order_info)  # Добавление в чек
                    total_price += quantity * int(price)
                    has_order = True  # Устанавливаем флаг, если есть 
        if has_order:
            total_label = QLabel(f"Итого: {total_price} руб.", self)
            self.cheque_box_layout.addWidget(total_label)
            self.cheque_box_widget.show()  # Показываем чек, если есть выбранные блюда
        else:
            self.cheque_box_widget.hide()  # Скрываем чек, если ничего не выбрано
            self.setGeometry(300, 300, 300, 360)

        self.cheque_box_layout.addStretch()
        
    # поля ввода количества отключены при убранном чекбоксе   
    def count(self):
        for check_box, (input_box, price) in self.input_boxes.items():
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