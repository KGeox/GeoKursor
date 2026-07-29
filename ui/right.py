from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget
import os
from core.cursor_apply import apply_cursor
from .central import central

current_dir = os.path.dirname(os.path.abspath(__file__))
packs_dir = os.path.join(current_dir,"../data/cursorpacks")

class right(QWidget):
    def __init__(self, central_instance):
        super().__init__()
        self.central = central_instance



