#File used to practice using the PyQt library

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


#App Settings

app = QApplication([])
main_window = QWidget
main_window.setWindowTitle('First Test App')
main_window.resize(300, 200)

