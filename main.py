import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QGridLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from assets import ButtonHolder, left_side

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GeoKursor')
        self.resize(900, 600)

        container = QWidget()
        self.setCentralWidget(container)

        layout = QGridLayout()

        layout.addWidget(left_side(), 0, 0)
        layout.addWidget(left_side(),0, 1)
        layout.addWidget(left_side(), 0, 2)

        container.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) ## Start event loop

if __name__ == "__main__":
    main()

