import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QRadioButton

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

def center():
    inner_container = QWidget()
    inner_layout = QVBoxLayout(inner_container)

    for i in range(10):
        inner_layout.addWidget(QRadioButton(str(i)))

    return inner_container

def right_side():
    inner_container = QWidget()
    inner_layout = QVBoxLayout(inner_container)

    in_inner_container = QWidget()
    in_inner_layout = QHBoxLayout(in_inner_container)

    preview_but = QPushButton('Preview')

    Apply_on_arrow = QPushButton('Apply on arrow')
    Apply_all = QPushButton('Apply all')


    in_inner_layout.addWidget(Apply_on_arrow)
    in_inner_layout.addWidget(Apply_all)
    inner_layout.addWidget(preview_but)
    inner_layout.addWidget(in_inner_container)

    return inner_container