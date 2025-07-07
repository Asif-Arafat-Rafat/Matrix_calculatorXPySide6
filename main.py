import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
app=QApplication(sys.argv)
window =QMainWindow()
window.setWindowTitle("My App")
button=QPushButton("Click me")
button.setText("Click me111")
window.setCentralWidget(button)
window.show()
app.exec()