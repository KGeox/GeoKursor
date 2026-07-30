from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QMainWindow, QPushButton, QListWidget
import os
from core.cursor_apply import apply_cursor

current_dir = os.path.dirname(os.path.abspath(__file__))
packs_dir = os.path.join(current_dir,"../data/cursorpacks")

class central(QMainWindow):
    def __init__(self):
        super().__init__()


        container = QWidget()
        self.setCentralWidget(container)

        self.inner_layout2 = QGridLayout(container)

        #Right
        self.inner_layout = QVBoxLayout()

        self.in_inner_container = QWidget()
        self.in_inner_layout = QHBoxLayout(self.in_inner_container)

        self.theme_list = QListWidget()
        self.theme_list.addItems(os.listdir(packs_dir))
        self.selected_cursor = self.theme_list.itemClicked.connect(self.give_name)

        self.preview_but = QPushButton('Preview')

        self.Apply_on_arrow_but = QPushButton('Apply on arrow')

        self.Apply_all_but = QPushButton('Apply all')
        self.Apply_all_but.clicked.connect(lambda: print("The settings where applied to all cur"))

        self.Apply_on_arrow_but.clicked.connect(lambda:apply_cursor(str(self.cur_path +"/" +str(self.selected_cursor))))

        self.in_inner_layout.addWidget(self.Apply_on_arrow_but)
        self.in_inner_layout.addWidget(self.Apply_all_but)
        self.inner_layout.addWidget(self.theme_list)
        self.inner_layout.addWidget(self.preview_but)
        self.inner_layout.addWidget(self.in_inner_container)


        # Center
        self.list_widget = QListWidget()

        self.list_widget.addItems(os.listdir(packs_dir))
        self.selected_pac = self.list_widget.itemClicked.connect(self.give_name2)

        # self.list_widget.itemClicked.connect(self.give_name)


        self.inner_layout2.addWidget(self.list_widget, 0, 0)
        self.inner_layout2.addLayout(self.inner_layout, 0,1)
        # container.setLayout(self.inner_layout2)

    def give_name2(self, item):
        self.selected_pac = item.text()

        self.cur_path = os.path.join(packs_dir,self.selected_pac)
        self.theme_list.clear()
        # self.theme_list = os.listdir(self.cur_path)
        self.theme_list.addItems(os.listdir(self.cur_path))
        print(self.theme_list)

        return self.cur_path

    def give_name(self, item):
        self.selected_cursor = item.text()
        print(self.selected_cursor)
        return self.selected_cursor



