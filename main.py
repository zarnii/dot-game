import sys

from PyQt5 import QtWidgets
from main_form import Ui_MainWindow


if __name__ == '__main__':
	#Create applications
	app = QtWidgets.QApplication([sys.argv])

	#Create form and init it
	mainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(mainWindow)
	mainWindow.show()

	#Run main loop
	sys.exit(app.exec())