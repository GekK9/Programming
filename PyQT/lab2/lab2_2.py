import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lab2_2.ui', self)
        self.pushButton_add.clicked.connect(self.add_contact)
        
    def add_contact(self):
        self.name = self.lineEdit_name.text()
        self.phone = self.lineEdit_phone.text()
        self.listWidget.addItem(self.name + ' ' + self.phone)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())