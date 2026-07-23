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

    listwidget = QListWidget()
    listwidget.addItems(['One', 'Two', 'Three'])
    inner_layout.addWidget(listwidget)

    return inner_container

def right_side():
    inner_container = QWidget()
    inner_layout = QVBoxLayout(inner_container)

    in_inner_container = QWidget()
    in_inner_layout = QHBoxLayout(in_inner_container)

    preview_but = QPushButton('Preview')

    Apply_on_arrow_but = QPushButton('Apply on arrow')
    Apply_all_but = QPushButton('Apply all')
    Apply_all_but.clicked.connect(lambda: print("The settings where applied to all cur"))
    Apply_on_arrow_but.clicked.connect(lambda: print("It has only been applied to arrow"))


    in_inner_layout.addWidget(Apply_on_arrow_but)
    in_inner_layout.addWidget(Apply_all_but)
    inner_layout.addWidget(preview_but)
    inner_layout.addWidget(in_inner_container)

    return inner_container