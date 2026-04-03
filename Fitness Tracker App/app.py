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
        self.initUI()

    #Settings
    def settings(self):
        self.setWindowTitle("FitTrack")
        self.resize(800,600)

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
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Id", "Date", "Calories", "Distance", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        #Design the layout
        self.master_layout = QHBoxLayout()
        self.columnleft = QVBoxLayout()
        self.columnright = QVBoxLayout()

        self.subrowleft1 = QHBoxLayout()
        self.subrowleft2 = QHBoxLayout()
        self.subrowleft3 = QHBoxLayout()
        self.subrowleft4 = QHBoxLayout()

        self.subrowleft1.addWidget(QLabel("Date:"))
        self.subrowleft1.addWidget(self.date_box)

        self.subrowleft2.addWidget(QLabel("Calories:"))
        self.subrowleft2.addWidget(self.cal_box)

        self.subrowleft3.addWidget(QLabel("Distance (km):"))
        self.subrowleft3.addWidget(self.distance_box)

        self.subrowleft4.addWidget(QLabel("Description:"))
        self.subrowleft4.addWidget(self.description)

        #Add Left rows to the Left Column

        self.columnleft.addLayout(self.subrowleft1)
        self.columnleft.addLayout(self.subrowleft2)
        self.columnleft.addLayout(self.subrowleft3)
        self.columnleft.addLayout(self.subrowleft4)
        self.columnleft.addWidget(self.dark_box)


        button_row1 = QHBoxLayout()
        button_row2 = QHBoxLayout()

        button_row1.addWidget(self.add_button)
        button_row1.addWidget(self.delete_button)
        button_row2.addWidget(self.submit_button)
        button_row2.addWidget(self.clear_button)

        self.columnleft.addLayout(button_row1)
        self.columnleft.addLayout(button_row2)

        #Add right rows to right column
        self.columnright.addWidget(self.canvas)
        self.columnright.addWidget(self.table)


        #make master layout
        self.master_layout.addLayout(self.columnleft, 30)
        self.master_layout.addLayout(self.columnright, 70)
        self.setLayout(self.master_layout)
        
    #load tables

    #add tables

    #delete table

    #Calculate calories

    #click

    #dark mode

    #reset


#Init DB

if __name__ == "__main__":
    app =QApplication([])
    main = FitTrack()
    main.show()
    app.exec_()
