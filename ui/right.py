from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class right(QWidget):
    def __init__(self):
        super().__init__()

        self.inner_layout = QVBoxLayout(self)

        self.in_inner_container = QWidget()
        self.in_inner_layout = QHBoxLayout(self.in_inner_container)

        self.preview_but = QPushButton('Preview')

        self.Apply_on_arrow_but = QPushButton('Apply on arrow')
        self.Apply_all_but = QPushButton('Apply all')
        self.Apply_all_but.clicked.connect(lambda: print("The settings where applied to all cur"))
        self.Apply_on_arrow_but.clicked.connect(lambda: print("It has only been applied to arrow"))

        self.in_inner_layout.addWidget(self.Apply_on_arrow_but)
        self.in_inner_layout.addWidget(self.Apply_all_but)
        self.inner_layout.addWidget(self.preview_but)
        self.inner_layout.addWidget(self.in_inner_container)
