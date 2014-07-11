# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Jul  4 13:04:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 174)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.abrir_marcas = QtGui.QPushButton(self.centralwidget)
        self.abrir_marcas.setObjectName("abrir_marcas")
        self.gridLayout.addWidget(self.abrir_marcas, 0, 1, 1, 1)
        self.abrir_autos = QtGui.QPushButton(self.centralwidget)
        self.abrir_autos.setObjectName("abrir_autos")
        self.gridLayout.addWidget(self.abrir_autos, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.abrir_marcas.setText(QtGui.QApplication.translate("MainWindow", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.abrir_autos.setText(QtGui.QApplication.translate("MainWindow", "Autos", None, QtGui.QApplication.UnicodeUTF8))

