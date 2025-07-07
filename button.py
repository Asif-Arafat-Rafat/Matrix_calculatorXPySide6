from PySide6.QtWidgets import QMainWindow ,QApplication ,QPushButton
def button_clicked():
    print("Clicked")
def button_released():
    print("Released")
def button_pressed():
    print("Pressed")
def button_toggled(checked):
    print("Toggled",checked)
class Buttonholder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttonholder")
        button=QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(button_clicked)
        button.released.connect(button_released)
        button.pressed.connect(button_pressed)
        button.toggled.connect(button_toggled)
        # The order : Pressed,Toggled,Released,Clicked
        self.setCentralWidget(button)

