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
        self.settings()
        self.button_click()

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

        self.load_table()
    
    #Events
    def button_click(self):
        self.add_button.clicked.connect(self.add_workout)
        self.delete_button.clicked.connect(self.delete_workout)
        self.submit_button.clicked.connect(self.calculate_calories)
    #load tables
    def load_table(self):
        self.table.setRowCount(0)
        query = QSqlQuery("SELECT * FROM init ORDER BY date DESC")
        row = 0
        while query.next():
            fit_id = query.value(0)
            date = query.value(1)
            calories = query.value(2)
            distance = query.value(3)
            description = query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(fit_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(str(calories)))
            self.table.setItem(row, 3, QTableWidgetItem(str(distance)))
            self.table.setItem(row, 4, QTableWidgetItem(description))
            row += 1
            print("here too!")

    #add tables
    def add_workout(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        calories = self.cal_box.text()
        distance = self.distance_box.text()
        description = self.description.text()

        query = QSqlQuery("""
                        INSERT INTO init (date, calories, distance, description)
                        VALUES (?,?,?,?)  
                        """)
        query.addBindValue(date)
        query.addBindValue(calories)
        query.addBindValue(distance)
        query.addBindValue(description)
        query.exec_()

        self.date_box.setDate(QDate.currentDate())
        self.cal_box.clear()
        self.distance_box.clear()
        self.description.clear()

        self.load_table()
        print("made it here")

    #delete table
    def delete_workout(self):
        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a row to delete")

        fit_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Are you sure?", "Delete this workout?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return
        
        query = QSqlQuery()
        query.prepare("DELETE FROM init where id = ?")
        query.addBindValue(fit_id)
        query.exec_()

        self.load_table()
    #Calculate calories
    def calculate_calories(self):
        distances = []
        calories = []

        query = QSqlQuery("SELECT distance, calories FROM init ORDER BY calories ASC")
        while query.next():
            distance = query.value(0)
            calorie = query.value(1)
            distances.append(distance)
            calories.append(calorie)

        try:
            min_calorie = min(calories)
            max_calorie = max(calories)
            normalised_calories = [(calorie - min_calorie) / (max_calorie - min_calorie) for calorie in calories]
            
            plt.style.use("Solarize_Light2")
            ax = self.figure.subplots()
            ax.scatter(distances, calories, c=normalised_calories, cmap='viridis', label='Data Points')
            ax.set_title("Distance Vs. Calories")
            ax.set_xlabel("Distance")
            ax.set_ylabel("Calories")
            cbar = ax.figure.colorbar(ax.collections[0], label='Normalised Calories')
            ax.legend()
            self.canvas.draw()
        except Exception as e:
            print("ERROR:{e}")
            QMessageBox.warning(self, "Error", "Please enter some data first!")
    #click


    #dark mode

    #reset


#Init DB
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("init.db")

if not db.open():
    QMessageBox.critical(None, "ERROR", "DB NO OPEN >:(")
    exit(2)

query = QSqlQuery()
query.exec_("""
            CREATE TABLE IF NOT EXISTS init (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                calories REAL,
                distance REAL,
                description TEXT
            
            )
    """)


if __name__ == "__main__":
    app =QApplication([])
    main = FitTrack()
    main.show()
    app.exec_()
