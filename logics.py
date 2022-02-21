from PyQt5 import QtWidgets
#from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import main_form
import second_window
import third_window


class MainWindow(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.points = []
		self.moveTimer = QTimer(self)
		self.openButton.clicked.connect(self.open_second_window)
		self.secondOpenButton.clicked.connect(self.open_third_window)
		self.aLoadGame.triggered.connect(self.open_second_window)
		self.playButton.clicked.connect(self.play)
		self.stopButton.clicked.connect(self.stop)
		#self.moveTimer.timeout.connect(self.onMoveTimerTimeout)

	def mousePressEvent(self, e):
		print("Mouse pressed at", e.x(), e.y())
		if (e.x() % 20 == 0) and (e.y() % 20 == 0):
			self.points.append([e.x(), e.y()])
		self.update() 

	'''_________Create playground_________'''   
	def paintEvent(self, event):
		p = QPainter()
		p.begin(self)
		pen = QPen(Qt.black, 1)
		p.setPen(pen)

		
		x = 20
		while x <= 520:
			p.drawLine(x,100,x,500)
			x += 20

		y = 100
		while y < 520:
			p.drawLine(20,y,500,y)
			y += 20
		#painter.drawLine(10,200,510,200)

		'''_________Dot drawing_________'''	
		pen = QPen(Qt.red, 5)
		p.setPen(pen)
		for x, y in self.points:
			p.drawPoint(x, y)

		p.end()


	#функция открытия второго окна
	def open_second_window(self):
		self.twoWindow = TwoWindow()
		self.twoWindow.show()
		self.close()

	#функция открытия третьего окна
	def open_third_window(self):
		self.thirdwindow = ThirdWindow()
		self.thirdwindow.show()
		self.close()

	def play(self):
		self.moveTimer.start(100)

	def stop(self):
		self.moveTimer.stop()

	'''def onMoveTimerTimeout(self):
					#self.label.setGeometry(100,100,100,100)
					geom = self.label.geometry()
					self.label.setGeometry(geom.x(), (geom.y()+10) % self.centralwidget.height(), geom.width(), geom.height())'''


#Создание класса второго окна
class TwoWindow(QtWidgets.QMainWindow, second_window.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


#Создание класса третьего окна
class ThirdWindow(QtWidgets.QMainWindow, third_window.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
			