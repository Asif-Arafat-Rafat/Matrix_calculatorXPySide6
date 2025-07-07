from PySide6.QtWidgets import QMainWindow ,QSlider
from PySide6.QtCore import Qt

class Sliderholder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliderholder")
        slider=QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.setSingleStep(10)
        slider.setPageStep(20)
        slider.setTickInterval(10)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTracking(True)
        slider.valueChanged.connect(lambda data:print(f"Slider goes to:{data}"))
        self.setCentralWidget(slider)