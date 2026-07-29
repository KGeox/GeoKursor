from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
packs_dir = os.path.join(current_dir,"../data/cursorpacks")

class central(QWidget):
    def __init__(self):
        super().__init__()

        self.inner_layout = QVBoxLayout(self)

        self.list_widget = QListWidget()

        self.list_widget.addItems(os.listdir(packs_dir))

        self.list_widget.itemClicked.connect(self.give_name)


        self.inner_layout.addWidget(self.list_widget)

    def give_name(self, item):
        return item.text()

