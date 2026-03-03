from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from calculatorapp import app, text_box

#this is redundant as i was trying to import the function from this file

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
