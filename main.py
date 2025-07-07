import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from button import Buttonholder
from slider import Sliderholder
from inputbox import InputBox
app=QApplication(sys.argv)
# button=QPushButton("Click me")
# button.setText("Click me111")

main_window=QWidget()
main_window.setWindowTitle("Practice 1")
layout=QHBoxLayout()
layout.addWidget(Sliderholder())
layout.addWidget(Buttonholder())
layout.addWidget(InputBox())
main_window.setLayout(layout)
main_window.show()
app.exec()