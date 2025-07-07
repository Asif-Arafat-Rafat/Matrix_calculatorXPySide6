from PySide6.QtWidgets import QMainWindow ,QSlider,QWidget,QHBoxLayout
from PySide6.QtCore import Qt

class Sliderholder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliderholder")
        slider = QSlider(Qt.Vertical)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(lambda data:print(f"CHanged to:{data}"))
        layout = QHBoxLayout()
        layout.addWidget(slider)
        self.setLayout(layout)