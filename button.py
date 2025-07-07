from PySide6.QtWidgets import QMainWindow ,QApplication ,QPushButton
class Buttonholder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttonholder")
        button=QPushButton("Press Me")
        self.setCentralWidget(button)
