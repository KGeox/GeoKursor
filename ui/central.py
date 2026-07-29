from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from core.cursor_apply import apply_cursor
class central(QWidget):
    def __init__(self):
        super().__init__()

        self.inner_layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        # self.list_widget.addItems(apply_cursor(r"C:\Users\HP\PycharmProjects\GeoKursor\data\cursorpacks\Hollow Knight\Arrow.cur"))

        self.list_widget.itemClicked.connect(self.give_name)


        self.inner_layout.addWidget(self.list_widget)

    def give_name(self, item):
        return item.text()
