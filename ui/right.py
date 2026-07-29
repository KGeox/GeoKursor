from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
import os
from core.cursor_apply import apply_cursor

current_dir = os.path.dirname(os.path.abspath(__file__))
packs_dir = os.path.join(current_dir,"../data/cursorpacks/Hollow Knight")

class right(QWidget):
    def __init__(self, central_instance):
        super().__init__()
        self.central = central_instance
        self.inner_layout = QVBoxLayout(self)

        self.in_inner_container = QWidget()
        self.in_inner_layout = QHBoxLayout(self.in_inner_container)

        self.theme_list = QListWidget()
        self.theme_list.addItems(os.listdir(packs_dir))
        self.selected_cursor = self.theme_list.itemClicked.connect(self.give_name)


        self.preview_but = QPushButton('Preview')

        self.Apply_on_arrow_but = QPushButton('Apply on arrow')

        self.Apply_all_but = QPushButton('Apply all')
        self.Apply_all_but.clicked.connect(lambda: print("The settings where applied to all cur"))
        # self.Apply_on_arrow_but.clicked.connect(apply_cursor(os.path.join(str(packs_dir), str(self.selected_cursor))))

        self.in_inner_layout.addWidget(self.Apply_on_arrow_but)
        self.in_inner_layout.addWidget(self.Apply_all_but)
        self.inner_layout.addWidget(self.theme_list)
        self.inner_layout.addWidget(self.preview_but)
        self.inner_layout.addWidget(self.in_inner_container)

    def give_name(self, item):
        self.selected_cursor =item.text()
        print(self.selected_cursor)
        return self.selected_cursor

