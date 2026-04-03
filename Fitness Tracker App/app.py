#imports
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QDateEdit, QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
from sys import exit



# Main Class
class FitTrack (QWidget):
    
    def __init__(self):
        super().__init__()
    #initial UI
    def initUI(self):
        #All left column widgets
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.cal_box = QLineEdit()
        self.cal_box.setPlaceholderText("Number of Burned Calories")

        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("Enter Distance Ran")

        self.description = QLineEdit()
        self.description.setPlaceholderText("Type of Run")

        self.submit_button = QPushButton("Submit")
        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")
        self.clear_button = QPushButton("clear")
        self.dark_box = QCheckBox("Dark Mode")


        #All right column widgets
        self.table = QTableWidget()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)


    #load tables

    #add tables

    #delete table

    #Calculate calories

    #click

    #dark mode

    #reset


#Init DB