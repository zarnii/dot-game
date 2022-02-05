from PyQt5 import QtWidgets
import main_form
import second_window
import third_window


class MainWindow(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.openButton.clicked.connect(self.open_second_window)
		self.secondOpenButton.clicked.connect(self.open_third_window)
		self.aLoadGame.triggered.connect(self.open_second_window)

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
			