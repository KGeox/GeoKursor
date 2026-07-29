import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from assets import ButtonHolder, menu_bar
# from ui.left import left
from ui.central import central
from ui.right import right

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.left_side = left()
        self.central = central()
        self.right_side = right(self.central)

        self.setWindowTitle('GeoKursor')
        self.resize(900, 600)

        self.setMenuBar(menu_bar(self))

        container = QWidget()
        self.setCentralWidget(container)

        layout = QGridLayout()

        # layout.addWidget(self.left_side, 0, 0)
        layout.addWidget(self.central,0, 1)
        layout.addWidget(self.right_side, 0, 2)

        container.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) ## Start event loop

if __name__ == "__main__":
    main()

