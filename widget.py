from PyQt5.QtWidgets import (
	QPushButton, 
	QLabel, 
	QMessageBox,
    QHBoxLayout,
    QVBoxLayout,
    QToolButton
)
from PyQt5.QtGui import (
	QFont,
	QIcon
	)

def Button(text,window) : 
	
	return QPushButton(text,window)


def Text(text,window=None,size=14,family="Arial") : 

	label =  QLabel(text,window)
	font = QFont(family,size)
	label.setFont(font)
	label.adjustSize()
	return label

def Dialog(text,type="info") : 
	icon = QMessageBox.Information
	title = "Message"

	if type == "confirm" : 
		title = "confirm"
		icon = QMessageBox.Question

	if type == "waring" : 
		title = "Warning"
		icon = QMessageBox.Warning
	
	alert = QMessageBox()
	alert.setText(text)
	alert.setIcon(icon)
	alert.setWindowTitle(title)
	alert.exec()

def VLayout(ui=[]):
    layout = QVBoxLayout()
    for widget in ui:
        layout.addWidget(widget)
    return layout


def HLayout(ui=[]) : 
	layout = QHBoxLayout()
	for widget in ui : 
		layout.addWidget(widget)
	return layout

def IconButton(icon="",window=None,w=50,h=50) : 
	button = QToolButton(window)
	icon = QIcon(icon)
	button.setIcon(icon)
	button.setFixedSize(w,h)
	
	return button