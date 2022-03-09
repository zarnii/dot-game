from PyQt5 import QtWidgets
#from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import main_form
import second_window
import third_window
import menu


class MainWindow(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.firstPlayerPoints = []
		self.secondPlayerPoints = []
		self.player = 1

		self.mainWindowButton.clicked.connect(self.openMenuWindow)
		#self.moveTimer = QTimer(self)
		#self.openButton.clicked.connect(self.open_second_window)
		#self.secondOpenButton.clicked.connect(self.open_third_window)
		#self.aLoadGame.triggered.connect(self.open_second_window)
		#self.playButton.clicked.connect(self.play)
		#self.stopButton.clicked.connect(self.stop)
		#self.moveTimer.timeout.connect(self.onMoveTimerTimeout)

	def openMenuWindow(self):
		self.menuWindow = MenuWindow()
		self.menuWindow.show()
		self.close()

	def playerTurn(self):
		if self.player % 2 == 0:
			self.Player_turn.setText('Ходит игрок 2')
		elif self.player % 2 != 0:
			self.Player_turn.setText('Ходит игрок 1')


	def mousePressEvent(self, e):
		'''_____Round cords______'''
		x = round(e.x()/10)*10
		y = round(e.y()/10)*10
		print("Mouse pressed at", x, y)

		print("Mouse pressed at (round)", )
		if (x % 20 == 0) and (y % 20 == 0):
			if self.player % 2 == 0:
				self.player += 1
				self.Player_turn.setText('Ходит игрок 2')
				self.secondPlayerPoints.append([x, y])
				print('it was a second player')
				print(self.player)
				print(self.secondPlayerPoints)
				self.playerTurn()
				
			elif self.player % 2 != 0:
				self.player += 1
				self.firstPlayerPoints.append([x, y])
				print('it was a first player')
				print(self.player)
				print(self.firstPlayerPoints)
				self.playerTurn()

		self.update() 

	'''_________Create playground_________'''   
	def paintEvent(self, event):
		p = QPainter()
		p.begin(self)
		pen = QPen(Qt.black, 1)
		p.setPen(pen)

		
		x = 20
		while x < 520:
			p.drawLine(x,100,x,500)
			x += 20

		y = 100
		while y < 520:
			p.drawLine(20,y,500,y)
			y += 20
		#painter.drawLine(10,200,510,200)

		'''_________Dot drawing_________'''
		

		p = QPainter()
		p.begin(self)
		pen = QPen(Qt.blue, 5)
		p.setPen(pen)
		for x, y in self.secondPlayerPoints:
			p.drawPoint(x, y)
		p.end()
		
		p = QPainter()
		p.begin(self)
		pen = QPen(Qt.red, 5)
		p.setPen(pen)
		for x, y in self.firstPlayerPoints:
			p.drawPoint(x, y)
		p.end()

		for point in self.firstPlayerPoints:
			pass
			

	def open_second_window(self):
		self.twoWindow = TwoWindow()
		self.twoWindow.show()
		self.close()


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

class MenuWindow(QtWidgets.QMainWindow, menu.Ui_MainWindow):
	"""docstring for MenuWindow"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.playButton.clicked.connect(self.openMainWindow)
		self.closeButton.clicked.connect(self.close)
	
	def openMainWindow(self):
		self.mainWindow = MainWindow()
		self.mainWindow.show()
		self.close()

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

			