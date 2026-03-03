#File used to practice using the PyQt library

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from secondscreen import second_layout
from random import choice

#create functions

def changeScreen():
    #this function here is redundant as i was testing if i could manually overwrite a layout and essentially 'switch screens'
    main_window.setLayout(second_layout)

def changeWord1():
    #word should be a Qlabel
    title_1.setText(choice(my_words))

def changeWord2():
    #word should be a Qlabel
    title_2.setText(choice(my_words))

def changeWord3():
    #word should be a Qlabel
    title_3.setText(choice(my_words))

#App Settings

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("First Test App")
main_window.resize(300, 200)


#Create Objects/Widgets

my_words = ['purple', 'blue', 'red', 'yellow', 'green', 'orange', 'mandarin', 'broccoli']

title_text = QLabel("Find a random colour")
title_1 = QLabel('choice(my_words)')
title_2 = QLabel('choice(my_words)')
title_3 = QLabel('choice(my_words)')

button1 = QPushButton("New Colour!")
button2 = QPushButton("Spin the Wheel!")
button3 = QPushButton("I'm addicted to the colours!")


button1.clicked.connect(changeWord1)
button2.clicked.connect(changeWord2)
button3.clicked.connect(changeWord3)


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


#Import rows to master layout, then master layout to the main window

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

#Run the App
main_window.show()
app.exec_()


