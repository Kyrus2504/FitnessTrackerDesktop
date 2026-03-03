#File used to practice using the PyQt library

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


#App Settings

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("First Test App")
main_window.resize(300, 200)


#Create Objects/Widgets

title_text = QLabel("Pick your favourite colour")
title_1 = QLabel("Blue")
title_2 = QLabel("Red")
title_3 = QLabel("Purple")

button1 = QPushButton("This one!")
button2 = QPushButton("Its Red!")
button3 = QPushButton("Yes it has to be this!")


#Structure Layout
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

#Import created objects into the layout

row1.addWidget(title_text, alignment = Qt.AlignCenter)


row2.addWidget(title_1, alignment = Qt.AlignCenter)
row2.addWidget(title_2, alignment = Qt.AlignCenter)
row2.addWidget(title_3, alignment = Qt.AlignCenter)

row3.addWidget(button1, alignment = Qt.AlignCenter)
row3.addWidget(button2, alignment = Qt.AlignCenter)
row3.addWidget(button3, alignment = Qt.AlignCenter)


#Run the App
main_window.show()
app.exec_()