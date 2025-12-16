import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from util.widget import (Button, 
	HLayout, 
	VLayout, 
	Text, 
	IconButton,
	

	)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class Window(QMainWindow) : 
	def __init__(self) : 
		
		super().__init__() 
		self.setFixedSize(800,600)
		layout = VLayout([

			self.header(),
			self.footer()

		])
		layout.setContentsMargins(0,0,0,0)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		self.player = QMediaPlayer()

	def header(self) : 
		widget = QWidget()
		widget.setFixedHeight(450)
		widget.setStyleSheet("background-color: red")
		return widget

	def footer(self) : 
		widget = QWidget()
		uploadIcon = IconButton("icons/upload.png", None,50,50)
		uploadIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		uploadIcon.clicked.connect(self.upload)

		bkIcon = IconButton("icons/bk.png", None,50,50)
		bkIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")

		playIcon = IconButton("icons/play.png", None,100,100)
		playIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 50px; border: 1px solid #ddd")
		playIcon.clicked.connect(self.toggleMusic)

		fwIcon = IconButton("icons/fw.png", None,50,50)
		fwIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")

		stopIcon = IconButton("icons/stop.png", None,50,50)
		stopIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		stopIcon.clicked.connect(self.stop)

		layout = HLayout([

			uploadIcon,
			bkIcon,
			playIcon,
			fwIcon,
			stopIcon
			

		])


		widget.setFixedHeight(150)
		widget.setStyleSheet("background-color: white")
		widget.setLayout(layout)
		return widget

	def upload(self) : 
		path = QFileDialog.getOpenFileName(self,"Choose a file","","Audio File (*.mp3 *.ogg *.wav)")
		if path : 
			content = QMediaContent(QUrl.fromLocalFile(path[0]))
			self.player.setMedia(content)
			self.player.play()
			#QFileDialog.close(self)

	def toggleMusic(self) : 
		if self.player.mediaStatus() == QMediaPlayer.NoMedia : 
			self.upload()
			return False

		if self.player.state() == QMediaPlayer.PlayingState : 
			self.player.pause()

		elif self.player.state() == QMediaPlayer.PausedState : 
			self.player.play()
	
	def stop(self) : 
		if self.player.mediaStatus() == QMediaPlayer.NoMedia : 
			self.player.stop()

if __name__ == "__main__" : 
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec())







