import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow,)

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Programming\PyQT\lab3\lab3_1.ui', self)
        self.pushButton.clicked.connect(self.validate_password)
        self.label.setText("Введите пароль!")

    def validate_password(self):
        password = self.lineEdit.text()
        self.label_2.setText("")

        try:
            if len(password) <= 8:
                raise PasswordTooShort
            
            if ( not any(c.islower() for c in password) or (not any(c.isupper() for c in password))):
                raise NoMixedCase

            if not any(c.isdigit() for c in password):
                raise NoDigit

            keyboard_sequences = [
                'qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю',
                'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM',
                'ЙЦУКЕНГШЩЗХЪ', 'ФЫВАПРОЛДЖЭ', 'ЯЧСМИТЬБЮ',
            ]

            password_lower = password.lower()

            for seq in keyboard_sequences:
                for i in range(len(seq) - 2):
                    if seq[i:i+3].lower() in password_lower:
                        raise KeyboardSequenceDetected
            print("Пароль корректен")
            self.close()

        except PasswordTooShort:
            self.label_2.setText("Ошибка: Пароль слишком короткий (меньше 9 символов)")

        except NoMixedCase:
            self.label_2.setText("Ошибка: Пароль должен содержать буквы разного регистра")

        except NoDigit:
            self.label_2.setText("Ошибка: Пароль должен содержать хотя бы одну цифру")

        except KeyboardSequenceDetected:
            self.label_2.setText("Ошибка: Пароль содержит последовательность из 3 символов, идущих подряд на клавиатуре")

        except Exception as e:
            self.label_2.setText(f"Неизвестная ошибка: {str(e)}")

class PasswordTooShort(Exception):
    pass

class NoMixedCase(Exception):
    pass

class NoDigit(Exception):
    pass

class KeyboardSequenceDetected(Exception):
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())