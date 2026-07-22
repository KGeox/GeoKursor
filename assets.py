import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

def button_action(data):
    print("It works", data)

class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press")
        button.setCheckable(True) # to make a checkable button

        self.setCentralWidget(button)

        button.clicked.connect(button_action)


def left_side():
    inner_container = QWidget()
    inner_layout = QVBoxLayout(inner_container)

    Home_button = QPushButton('Home')
    Home_button.setCheckable(True)

    Settings_button = QPushButton('Settings')
    Settings_button.setCheckable(True)

    inner_layout.addWidget(Home_button)
    inner_layout.addWidget(Settings_button)

    return inner_container
