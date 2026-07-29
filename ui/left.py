from PySide6.QtWidgets import QWidget, QVBoxLayout,  QPushButton

class left(QWidget):

    def __init__(self):
        super().__init__()

        self.inner_layout = QVBoxLayout(self)

        self.Home_button = QPushButton('Home')
        self.Home_button.setCheckable(True)

        self.Settings_button = QPushButton('Settings')
        self.Settings_button.setCheckable(True)

        self.inner_layout.addWidget(self.Home_button)
        self.inner_layout.addWidget(self.Settings_button)

