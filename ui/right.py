from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
from core.cursor_apply import load_theme
from .central import central

class right(QWidget):
    def __init__(self, central_instance):
        super().__init__()
        self.central = central_instance
        self.inner_layout = QVBoxLayout(self)

        self.in_inner_container = QWidget()
        self.in_inner_layout = QHBoxLayout(self.in_inner_container)

        self.theme_list = QListWidget()
        self.preview_but = QPushButton('Preview')

        self.Apply_on_arrow_but = QPushButton('Apply on arrow')
        self.Apply_all_but = QPushButton('Apply all')
        self.Apply_all_but.clicked.connect(lambda: print("The settings where applied to all cur"))
        self.Apply_on_arrow_but.clicked.connect(lambda: print("It has only been applied to arrow"))

        self.in_inner_layout.addWidget(self.Apply_on_arrow_but)
        self.in_inner_layout.addWidget(self.Apply_all_but)
        self.inner_layout.addWidget(self.theme_list)
        self.inner_layout.addWidget(self.preview_but)
        self.inner_layout.addWidget(self.in_inner_container)

        self.central.list_widget.itemClicked.connect(self.update_view)

    def update_view(self, item):
        theme_name = item.text()
        self.theme_list.clear()
        files = load_theme(theme_name)
        self.theme_list.addItems(files)