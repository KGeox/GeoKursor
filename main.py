import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('GeoKursor')

        label = QLabel('Hello World')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

