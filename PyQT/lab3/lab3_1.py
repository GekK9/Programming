import re
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow)

class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Programming\PyQT\lab3\lab3_1.ui', self)
        self.lineEdit.setPlaceholderText("Например: +7(902)123-4567")
        self.pushButton.clicked.connect(self.validate_phone)

    def validate_phone(self):
        phone = self.lineEdit.text().strip()
        cleaned = re.sub(r'\s', '', phone)
        pattern = r'^(\+7|8)(\(?\d{3}\)?)?[\d\-]*\d$'

        if not re.fullmatch(pattern, cleaned):
            self.label_2.setText("error")
            return

        if (cleaned.count('(') != cleaned.count(')')) or (cleaned.count('(') > 1):
            self.label_2.setText("error")
            return

        if '-' in cleaned:
            if cleaned.startswith('-') or cleaned.endswith('-') or '--' in cleaned:
                self.label_2.setText("error")
                return

        digits = re.sub(r'\D', '', cleaned)

        if digits.startswith('8'):
            digits = '+7' + digits[1:]
        elif digits.startswith('7'):
            digits = '+' + digits

        if len(digits) != 12:  # + и 11 цифр
            self.label_2.setText("error")
            return
        self.lineEdit.setText(digits)
        self.label_2.setText('Номер добавлен!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())