import sys
import os
from PyQt5.QtWidgets import (
	QApplication, 
	QMainWindow, 
	QWidget, 
	QFileDialog,
	QSlider
	
	)

from util.widget import (Button, 
	HLayout, 
	VLayout, 
	Text, 
	IconButton,
	

	)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon

class Footer : 
	def __init__(self) : 
		widget = QWidget()
		widget.setFixedHeight(180)
		widget.setStyleSheet("background-color : white")
		return widget

class Window(QMainWindow) : 
	def __init__(self) : 
		
		super().__init__() 
		icon = QIcon("icons/music.png")
		self.setFixedSize(800,600)
		self.setWindowTitle("Music 0.0.1")
		self.setWindowIcon(icon)
		layout = VLayout([

			self.header(),
			self.footer()

		])
		layout.setContentsMargins(0,0,0,0)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		self.player = QMediaPlayer()
		self.player.mediaStatusChanged.connect(self.mediaStatus)
		self.player.positionChanged.connect(self.playedDuration)

	def header(self) : 
		widget = QWidget()
		widget.setFixedHeight(420)
		widget.setStyleSheet("background-color: red")
		self.title = Text("Choose a Song",widget,40,'Open Sans')
		self.title.move(200,200)
		return widget

	def footer(self) : 
		widget = QWidget()
		self.timestamp = Text("0.0",widget)
		self.timestamp.move(10,40)

		slash = Text("/",widget)
		slash.move(50,50)

		self.duration = Text("0.0",widget)
		self.duration.move(80,40)

		self.volumeIcon = IconButton("icons/volume.png", None,50,50)
		self.volumeIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		self.volumeIcon.clicked.connect(self.volume)

		bkIcon = IconButton("icons/bk.png", None,50,50)
		bkIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		bkIcon.clicked.connect(self.backward)

		self.playIcon = IconButton("icons/play.png", None,100,100)
		self.playIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 50px; border: 1px solid #ddd")
		self.playIcon.clicked.connect(self.toggleMusic)

		fwIcon = IconButton("icons/fw.png", None,50,50)
		fwIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		fwIcon.clicked.connect(self.forward)

		stopIcon = IconButton("icons/stop.png", None,50,50)
		stopIcon.setStyleSheet("background-color : #f5f5f5; border-radius : 25px; border: 1px solid #ddd")
		stopIcon.clicked.connect(self.stop)

		self.slider = QSlider(Qt.Horizontal,widget)
		self.slider.setGeometry(50,50,200,30)
		self.slider.sliderMoved.connect(self.onSlide)
		self.slider.sliderReleased.connect(self.sliderLeave)


		layout = HLayout([

			self.volumeIcon,
			bkIcon,
			self.playIcon,
			fwIcon,
			stopIcon
			

		])

		alignLayout = VLayout([self.slider])
		alignLayout.addLayout(layout)

		widget.setFixedHeight(150)
		widget.setStyleSheet("background-color: white")
		widget.setLayout(alignLayout)
		return widget

	def upload(self) : 
		path = QFileDialog.getOpenFileName(self,"Choose a file","","Audio File (*.mp3 *.ogg *.wav)")
		if path : 
			content = QMediaContent(QUrl.fromLocalFile(path[0]))
			self.player.setMedia(content)
			self.player.play()

			if self.player.state() == QMediaPlayer.PlayingState :
				filename = os.path.basename(path[0])
				self.playIcon.setIcon(QIcon("icons/pause.png"))
				self.title.setText(filename)


			#QFileDialog.close(self)

	def toggleMusic(self) : 
		if self.player.mediaStatus() == QMediaPlayer.NoMedia : 
			self.upload()
			return False

		if self.player.state() == QMediaPlayer.PlayingState : 
			self.player.pause()
			self.playIcon.setIcon(QIcon("icons/play.png"))

		elif self.player.state() == QMediaPlayer.PausedState : 
			self.player.play()
			self.playIcon.setIcon(QIcon("icons/pause.png"))

		else : 
			self.player.play()
			self.playIcon.setIcon(QIcon("icons/pause.png"))
	
	def stop(self) : 
		if self.player.mediaStatus() == QMediaPlayer.NoMedia : 
			self.player.stop()
			self.player.setPosition(0)
			self.player.setMedia(QMediaContent())
			self.playIcon.setIcon(QIcon("icons/play.png"))

	def volume(self) : 
		if self.player.isMuted() : 
			self.player.setMuted(False)
			self.volumeIcon.setIcon(QIcon("icons/volume.png"))
		else : 
			self.player.setMuted(True)
			self.volumeIcon.setIcon(QIcon("icons/mute.png"))

	def forward(self) : 
		currentDuration = self.player.position() + 10000
		self.player.setPosition(currentDuration)
		currentSlideValue = self.slider.value()
		self.slider.setValue(currentSlideValue+10)

    
	def backward(self) : 
		currentDuration = max(self.player.position() - 10000,0)
		self.player.setPosition(currentDuration)
		currentSlideValue = self.slider.value()
		self.slider.setValue(currentSlideValue-10)

	def onSlide(self,value) : 
		self.player.setPosition(value)
		self.player.setMuted(True)

	def mediaStatus(self,status) : 
		if status == QMediaPlayer.BufferedMedia : 
			duration = self.player.duration()
			minute = round(duration/60000,1)
			self.duration.setText(str(minute))
			self.slider.setMaximum(duration)

	def playedDuration(self,position) : 
		minute = round(position/60000,1)
		self.timestamp.setText(str(minute))
		self.slider.setValue(position)
		if self.player.state() == 0 : 
			self.player.setPosition(0)
			self.playIcon.setIcon(QIcon("icons/play.png"))


	def sliderLeave(self) : 
		self.slider.setMuted(False)

if __name__ == "__main__" : 
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec())







