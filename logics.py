from PyQt5 import QtWidgets
# from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


import main_form
import menu
#from test import arr


class MainWindow(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.firstPlayerPoints = []
		self.secondPlayerPoints = []

		self.firstConnectedList = []
		self.secondConnectedList = []

		self.firstPlayerScore = 0
		self.secondPlayerScore = 0

		self.player = 1

		self.mainWindowButton.clicked.connect(lambda: self.openMenuWindow())

	# self.moveTimer = QTimer(self)
	# self.openButton.clicked.connect(self.open_second_window)
	# self.secondOpenButton.clicked.connect(self.open_third_window)
	# self.aLoadGame.triggered.connect(self.open_second_window)
	# self.playButton.clicked.connect(self.play)
	# self.stopButton.clicked.connect(self.stop)
	# self.moveTimer.timeout.connect(self.onMoveTimerTimeout)

	# Возвращение в главное меню из игрового меню
	def openMenuWindow(self):
		self.menuWindow = MenuWindow()
		self.menuWindow.show()
		self.close()

	# Выводит на экран ход игрока
	def playerTurn(self):
		if self.player % 2 == 0:
			self.Player_turn.setText('Ходит игрок 2')
		elif self.player % 2 != 0:
			self.Player_turn.setText('Ходит игрок 1')
		self.secondScoreLabel.setText(f'2: {self.secondPlayerScore}')
		self.firstScoreLabel.setText(f'1: {self.firstPlayerScore}')
			
	'''def getScore(self):
					if self.player % 2 == 0:
						self.secondScoreLabel.setText(f'2: {self.secondPlayerScore}')
					elif self.player % 2 != 0:
						self.firstScoreLabel.setText(f'1: {self.firstPlayerScore}')'''

	'''
	   Идет отслежование нажатий мышки на экран 
	   и эти координаты добовляюся в списки	
	'''

	def mousePressEvent(self, e):
		#self.getScore()
		x = round(e.x() / 10) * 10
		y = round(e.y() / 10) * 10
		print("Mouse pressed at", x, y)

		x_y_in_firstPlayerPoints = False
		x_y_in_secondPlayerPoints = False

		if x >= 20 and x <= 500 and y >= 100 and x <= 500:
			if (x % 20 == 0) and (y % 20 == 0):
				if self.player % 2 == 0:
					self.player += 1

					# Идет проверка на наличе на этом месте точки
					for i in self.firstPlayerPoints:
						if x == i[0] and y == i[1]:
							x_y_in_firstPlayerPoints = True
					for i in self.secondPlayerPoints:
						if x == i[0] and y == i[1]:
							x_y_in_secondPlayerPoints = True
					print('нажал второй игрок')

					# Если на этом месте нет точки, то создать ее там
					if x_y_in_firstPlayerPoints == False and x_y_in_secondPlayerPoints == False:
						self.secondPlayerPoints.append([x, y])
						print('\nЭто место свободно!')
						print('Координаты добавились')
						# print(self.player)
						print(f'{self.secondPlayerPoints} - точки второго игрока')
						tempList = self.findConnectList(self.secondPlayerPoints,[x,y])
						for pnt in tempList:
							self.secondConnectedList.append(pnt)
						#self.playerTurn()
						print(self.secondConnectedList)


					else:
						print('Это место уже занято!')


				elif self.player % 2 != 0:
					self.player += 1

					# Идет проверка на наличе на этом месте точки
					for i in self.firstPlayerPoints:
						if x == i[0] and y == i[1]:
							x_y_in_firstPlayerPoints = True
					for i in self.secondPlayerPoints:
						if x == i[0] and y == i[1]:
							x_y_in_secondPlayerPoints = True
					print('нажал первый игрок')

					# Если на этом месте нет точки, то создать ее там
					if x_y_in_firstPlayerPoints == False and x_y_in_secondPlayerPoints == False:
						print('\nЭто место свободно!')
						self.firstPlayerPoints.append([x, y])
						print('Координаты добавились')
						print(f'{self.firstPlayerPoints} - очки первого игрока')
						tempList = self.findConnectList(self.firstPlayerPoints, [x, y])
						for pnt in tempList:
							self.firstConnectedList.append(pnt)
						#self.playerTurn()
						print(self.firstConnectedList)
						#print(self.connectedList)

					else:
						print('Это место уже занято!')
		if len(self.firstConnectedList) != 0:
			self.firstPlayerScore = len(self.firstConnectedList)
		print(f'{self.firstPlayerScore} - очки первого игрока')
		if len(self.secondConnectedList) != 0:
			self.secondPlayerScore = len(self.secondConnectedList)
		print(f'{self.secondPlayerScore} - очки второго игрока')
		self.playerTurn()
		self.update()



	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawPlayGround(qp)
		self.drawDot(qp)
		self.dotConnect(qp,)
		qp.end()

	def dotConnect(self, qp):
		if self.firstConnectedList != []:
			pen = QPen(Qt.red, 2)
			qp.setPen(pen)
			for i in self.firstConnectedList:
				first_dot = i[0]
				x_first_dot = first_dot[0]
				y_first_dot = first_dot[1]

				second_dot = i[1]
				x_second_dot = second_dot[0]
				y_second_dot = second_dot[1]

				qp.drawLine(x_first_dot, y_first_dot, x_second_dot, y_second_dot)

		if self.secondConnectedList != []:
			pen = QPen(Qt.blue, 2)
			qp.setPen(pen)
			for i in self.secondConnectedList:
				first_dot = i[0]
				x_first_dot = first_dot[0]
				y_first_dot = first_dot[1]

				second_dot = i[1]
				x_second_dot = second_dot[0]
				y_second_dot = second_dot[1]

				qp.drawLine(x_first_dot, y_first_dot, x_second_dot, y_second_dot)




	def drawDot(self, qp):
		pen = QPen(Qt.blue, 5)
		qp.setPen(pen)
		for x, y in self.secondPlayerPoints:
			qp.drawPoint(x, y)

		pen = QPen(Qt.red, 5)
		qp.setPen(pen)
		for x, y in self.firstPlayerPoints:
			qp.drawPoint(x, y)

	def drawPlayGround(self, qp):
		x = 20
		while x < 520:
			qp.drawLine(x, 100, x, 500)
			x += 20

		y = 100
		while y < 520:
			qp.drawLine(20, y, 500, y)
			y += 20

	# painter.drawLine(10,200,510,200)
	def findConnectList(self, dotList, startPoint):
		usedPoints = []
		q = []
		q.append([startPoint,0])
		usedPoints.append(startPoint)
		fromList = []
		resultList =[]
		while len(q):
			currentVertex = q.pop(0)
			currentPoint = currentVertex[0]
			fromPoint = currentVertex[1]
			for dt in dotList:
				if dt==fromPoint:
					continue
				if ((dt[0] + 20 == currentPoint[0]) and (dt[1] == currentPoint[1])) or (
					(dt[0] - 20 == currentPoint[0]) and (dt[1] == currentPoint[1])) or (
					(dt[0] == currentPoint[0]) and (dt[1] + 20 == currentPoint[1])) or (
					(dt[0] == currentPoint[0]) and (dt[1] - 20 == currentPoint[1])) or (
					(dt[0] + 20 == currentPoint[0]) and (dt[1] + 20 == currentPoint[1])) or (
					(dt[0] + 20 == currentPoint[0]) and (dt[1] - 20 == currentPoint[1])) or (
					(dt[0] - 20 == currentPoint[0]) and (dt[1] + 20 == currentPoint[1])) or (
					(dt[0] - 20 == currentPoint[0]) and (dt[1] - 20 == currentPoint[1])):
					if dt in usedPoints:
						resultList.append([dt,currentPoint])
						v = dt
						while v != None:
							fromV = None
							for f in fromList:
								if f[0] == v:
									fromV = f[1]
									break
							if (fromV!=None):
								resultList.append([fromV,v])
							v=fromV
						v = currentPoint
						while v != None:
							fromV = None
							for f in fromList:
								if f[0] == v:
									fromV = f[1]
									break
							if (fromV != None):
								resultList.append([fromV, v])
							v = fromV
					else:
						usedPoints.append(dt)
						q.append([dt,currentPoint])
						fromList.append([dt,currentPoint])

		n = []
		for i in resultList:
			if i not in n:
				n.append(i)
		#return resultList
		return n


# Главное меню всего приложения
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
