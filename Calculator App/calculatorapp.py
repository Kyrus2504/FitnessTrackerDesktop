from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit



app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Calc, which is short for Calculator btw')
main_window.resize(300, 400)



#Create Objects
grid = QGridLayout()
master_layout = QVBoxLayout()
text_box = QLineEdit()

number1 = QPushButton('1')
number2 = QPushButton('2')
number3 = QPushButton('3')
number4 = QPushButton('4')
number5 = QPushButton('5')
number6 = QPushButton('6')
number7 = QPushButton('7')
number8 = QPushButton('8')
number9 = QPushButton('9')
number0 = QPushButton('0')

operatorPlus = QPushButton('+')
operatorMinus = QPushButton('-')
operatorMult = QPushButton('*')
operatorDiv = QPushButton('/')

decimal = QPushButton('.')

clearButton = QPushButton('Clear')
deleteButton = QPushButton('Del')

signEquals = QPushButton ('=')

#Function
def button_click():

    button = app.sender()
    text = button.text()


    if text == '=':
        symbol = text_box.text()
        try:
            res = eval(symbol)
            text_box.setText(str(res))
        except Exception as e:
            text_box.setText("error")

    elif text == 'Clear':
        text_box.clear()
    
    elif text == 'Del':
        current_text = text_box.text()
        text_box.setText(current_text[:-1])
    else:
        current_text = text_box.text()
        text_box.setText(current_text + text)


#import objects to layout
#Top Row
grid.addWidget(number7, 0, 0)
grid.addWidget(number8, 0, 1)
grid.addWidget(number9, 0, 2)
grid.addWidget(operatorPlus, 0, 3)

#Second Row
grid.addWidget(number4, 1, 0)
grid.addWidget(number5, 1, 1)
grid.addWidget(number6, 1, 2)
grid.addWidget(operatorMinus, 1, 3)

#Third Row
grid.addWidget(number1, 2, 0)
grid.addWidget(number2, 2, 1)
grid.addWidget(number3, 2, 2)
grid.addWidget(operatorMult, 2, 3)

#Fourth Row
grid.addWidget(number0, 3, 0)
grid.addWidget(decimal, 3, 1)
grid.addWidget(signEquals, 3, 2)
grid.addWidget(operatorDiv, 3, 3)


bottomRow = QHBoxLayout()
bottomRow.addWidget(clearButton)
bottomRow.addWidget(deleteButton)


master_layout.addWidget(text_box)
master_layout.addLayout(grid)
master_layout.addLayout(bottomRow)


#Use functions (this can be shortened)
buttons = [number0, number1, number2, number3, number4, number5, number6, number7, number8, number9, operatorDiv, operatorMinus, operatorMult, operatorPlus,
           clearButton, deleteButton, signEquals, decimal]

for button in buttons:
    button.clicked.connect(button_click)


main_window.setLayout(master_layout)
main_window.show()
app.exec_()