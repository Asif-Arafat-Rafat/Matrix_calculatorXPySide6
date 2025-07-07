from PySide6.QtWidgets import QMainWindow ,QApplication ,QPushButton
def button_clicked():
    print("Clicked")
class Buttonholder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttonholder")
        button=QPushButton("Press Me")
        button.clicked.connect(button_clicked)
        self.setCentralWidget(button)

