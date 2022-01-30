import sys

from PyQt5 import QtWidgets
import main_form
import second_window
import third_window


#Создание класса основного окна
class MainWindow(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#self.twoWindow = None
		self.openButton.clicked.connect(self.open_second_window)
		self.secondOpenButton.clicked.connect(self.open_third_window)

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
			

if __name__ == '__main__':
	#Создание приложения
	app = QtWidgets.QApplication([sys.argv])

	#Запуск формы главного окна
	window = MainWindow()
	window.show()
	

	#Запуск
	sys.exit(app.exec())