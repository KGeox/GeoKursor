from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from core.cursor_loader import load_cursor_themes
class central(QWidget):
    def __init__(self):
        super().__init__()

        self.inner_layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        self.list_widget.addItems(load_cursor_themes())

        self.list_widget.itemClicked.connect(self.give_name)


        self.inner_layout.addWidget(self.list_widget)

    def give_name(self, item):
        return item.text()
