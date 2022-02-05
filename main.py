import sys
from PyQt5 import QtWidgets
from logics import MainWindow
			

if __name__ == '__main__':
	#Создание приложения
	app = QtWidgets.QApplication([sys.argv])

	#Запуск формы главного окна
	window = MainWindow()
	window.show()
	

	#Запуск
	sys.exit(app.exec())