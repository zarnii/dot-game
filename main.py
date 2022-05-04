import sys
from PyQt5 import QtWidgets
from logics import MenuWindow

			

if __name__ == '__main__':
	#Создание приложения
	app = QtWidgets.QApplication([sys.argv])

	#Запуск формы главного окна
	window = MenuWindow()
	window.show()
	

	#Запуск
	sys.exit(app.exec())