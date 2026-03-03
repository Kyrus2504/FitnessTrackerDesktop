#testing something with the buttons

#this file here is redundant as i was testing if i could manually overwrite a layout and essentially 'switch screens'

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


app = QApplication([])

second_layout = QVBoxLayout()

row1 = QHBoxLayout()

row1.addWidget(QLabel('Second Screen!'), Qt.AlignCenter)

second_layout.addLayout(row1)
