# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 538)
        MainWindow.setStyleSheet("QPushButton{\n"
"background-color: silver;\n"
"border-radius:10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:grey;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(20, 350, 171, 51))
        self.closeButton.setObjectName("closeButton")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(210, 350, 131, 51))
        self.openButton.setObjectName("openButton")
        self.secondOpenButton = QtWidgets.QPushButton(self.centralwidget)
        self.secondOpenButton.setGeometry(QtCore.QRect(360, 350, 141, 51))
        self.secondOpenButton.setObjectName("secondOpenButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aSaveGame = QtWidgets.QAction(MainWindow)
        self.aSaveGame.setObjectName("aSaveGame")
        self.aLoadGame = QtWidgets.QAction(MainWindow)
        self.aLoadGame.setObjectName("aLoadGame")
        self.menu.addAction(self.aSaveGame)
        self.menu.addAction(self.aLoadGame)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя игра"))
        self.label.setText(_translate("MainWindow", "Привет Мир!"))
        self.closeButton.setText(_translate("MainWindow", "close"))
        self.openButton.setText(_translate("MainWindow", "open"))
        self.secondOpenButton.setText(_translate("MainWindow", "open"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.aSaveGame.setText(_translate("MainWindow", "Сохранить"))
        self.aLoadGame.setText(_translate("MainWindow", "Загрузить"))