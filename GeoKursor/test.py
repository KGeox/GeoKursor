import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton, QCheckBox
#QVBoxLayout makes your things to be vertical
#QHBoxLayout the same as above but vertical
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GeoKursor')
        self.resize(900, 600)

        # 1. Création du conteneur central
        container = QWidget()
        self.setCentralWidget(container)

        # 2. Instanciation correcte du layout (avec parenthèses)
        layout = QGridLayout()

        # 3. Création et alignement des labels
        label1 = QLabel("One")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label2 = QLabel("Two")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label3 = QLabel("Three")
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label4 = QLabel("four")
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        buton = QPushButton("Clickme")

        line_edit = QLineEdit()
        text_edit = QTextEdit()

        combo_box = QComboBox()
        combo_box.addItems(['One', 'Two', 'Three'])

        listwidget = QListWidget()
        listwidget.addItems(['One', 'Two', 'Three'])

        listwidget.itemClicked.connect(lambda item: print(f"Item cliked {item.text()}"))
        listwidget.itemDoubleClicked.connect(lambda item: print(f'Item double-clicked{item.text()}'))

        inner_container = QWidget()

        inner_layout = QHBoxLayout(inner_container)

        checkbox1 = QCheckBox('One')
        checkbox2 = QCheckBox('Two')
        checkbox3 = QCheckBox('Three')

        radio1 = QRadioButton('one')
        radio2 = QRadioButton('Two')

        for r in (radio1, radio2):
            r.toggled.connect(self.radio_changed)

        slider = QSlider()
        slider.setRange(0, 100)

        inner_layout.addWidget(checkbox1)
        inner_layout.addWidget(checkbox2)
        inner_layout.addWidget(checkbox3)

        # 4. Ajout des widgets au layout
        layout.addWidget(label4, 0,0)
        layout.addWidget(label1,0, 1)
        layout.addWidget(label2,1, 0)
        layout.addWidget(label3, 1, 1)
        layout.addWidget(buton)
        layout.addWidget(line_edit)
        layout.addWidget(text_edit)
        layout.addWidget(combo_box)
        layout.addWidget(listwidget)
        layout.addWidget(inner_container)
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        layout.addWidget(slider)


        # 5. Application du layout au conteneur
        container.setLayout(layout)

    def radio_changed(self):
        r = self.sender()
        if r is not None and r.isChecked():
            print('Radio button was selecteed! Value' + r.text())



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# Start event loop
if __name__ == "__main__":
    main()
