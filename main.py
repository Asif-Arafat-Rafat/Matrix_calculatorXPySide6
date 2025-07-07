import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from button import Buttonholder
app=QApplication(sys.argv)
# button=QPushButton("Click me")
# button.setText("Click me111")
window=Buttonholder()
window.show()
app.exec()