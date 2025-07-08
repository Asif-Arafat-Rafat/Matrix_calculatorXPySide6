from PySide6.QtWidgets import QWidget,QLineEdit,QLabel,QVBoxLayout,QPushButton
import sys
def print1(test):
    print(test)
class InputBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input box here")
        self.setGeometry(0,0,300,100)
        self.test=QLineEdit()
        self.test.setMinimumSize(20,20)
        self.test.setMaximumSize(200,200)
        button=QPushButton("Enter")
        button.clicked.connect(lambda:print1(self.test.text()))
        layout=QVBoxLayout()
        layout.addWidget(self.test)
        layout.addWidget(button)
        self.setLayout(layout)