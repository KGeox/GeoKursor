import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QComboBox, QRadioButton
from functionalities import Apply_all

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



def menu_bar(window_instance):

    menubar = window_instance.menuBar()

    fileMenu = menubar.addMenu('file')
    editMenu = menubar.addMenu('edit')
    helpMenu =menubar.addMenu('help')

    submenu = fileMenu.addMenu('submenu')
    exitAction = submenu.addAction('Exit')
    exitAction.triggered.connect(QApplication.instance().quit)

    background_menu = editMenu.addMenu('background Color')
    darkth_switch = background_menu.addAction('dark theme')
    lightth_switch = background_menu.addAction('light theme')
    systemth_switch = background_menu.addAction('System theme')

    git_repo = helpMenu.addAction('Access it repo')



    return menubar
