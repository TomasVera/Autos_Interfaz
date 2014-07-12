# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Main_ui import Ui_MainWindow
import Marcas
import Autos
import os


class Main(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		self.connect_actions()

	def connect_actions(self):
		self.ui.abrir_marcas.clicked.connect(self.action_abrir_marcas)
		self.ui.abrir_autos.clicked.connect(self.action_abrir_autos)

	def action_abrir_marcas(self):
		self.setVisible(False)
		self.marcasWindow = Marcas.Marcas()
		self.marcasWindow.exec_()
	
	def action_abrir_autos(self):
		self.setVisible(False)
		self.autosWindow = Autos.Autos()
		self.autosWindow.exec_()
		

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
