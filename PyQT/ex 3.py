from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QPushButton, QLineEdit
import sys, string

class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window
        self.setGeometry(300, 300, 395, 120)
        self.setWindowTitle('Азбука морзе')

        # taking alphabet
        alph = string.ascii_lowercase
        

        # create letter buttons
        for i, letter in enumerate(alph[:15]):
            button = QPushButton(letter, self)
            button.setFixedSize(25, 25)
            button.move((i * 25) + 10, 10)
            button.clicked.connect(self.run)
            
        for i, letter in enumerate(alph[15:]):
            button = QPushButton(letter, self)
            button.setFixedSize(25, 25)
            button.move((i * 25) + 10, 35)
            button.clicked.connect(self.run)

        # create text box
        self.text_box = QLineEdit(self)
        self.text_box.resize(370, 25)
        self.text_box.move(10, 75)

        self.morse_text = ''
        
        # set text to text box
    def run(self):
        self.morse_text += (f"{self.to_morse(self.sender().text())} ")
        self.text_box.setText(self.morse_text)

        # traslate letter to morse code
    def to_morse(self, s):
        morse = {
        'a': '.-', 'b': '-...', 'c': '-.-.',
        'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-','r': '.-.',
        's': '...', 't': '-', 'u': '..-',
        'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..',
        }
        return morse.get(s)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())


