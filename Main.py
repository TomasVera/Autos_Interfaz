# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from Main_ui import Ui_MainWindow
import Marcas
import Autos
import os
import controller


class Main(QtGui.QMainWindow):
	isLoged = False
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		self.connect_actions()
		self.setGeometry(300,150,self.width(),self.height())
		self.ui.le2.setEchoMode(QtGui.QLineEdit.Password)
		self.ui.ventanas.setEnabled(False)
		self.setMaximumHeight(self.height()-1)
		self.setMaximumWidth(self.width()-1)

	def connect_actions(self):
		self.ui.abrir_marcas.clicked.connect(self.action_abrir_marcas)
		self.ui.abrir_autos.clicked.connect(self.action_abrir_autos)
		self.ui.cancelBtn.clicked.connect(self.salir)
		self.ui.okBtn.clicked.connect(self.aceptar)

	def action_abrir_marcas(self):
		self.setVisible(False)
		self.marcasWindow = Marcas.Marcas()
		self.marcasWindow.exec_()
	
	def action_abrir_autos(self):
		self.setVisible(False)
		self.autosWindow = Autos.Autos()
		self.autosWindow.exec_()
		
	def salir(self):
		exit()
	def aceptar(self):
		'''Método que verifica si los campos rellenados son correctos, en tal caso, cierra la ventana 'login' y abre la ventana principal'''
		datos = controller.getUsuarios()
		for row in datos:
			if(row['username']==str(self.ui.le1.text()) and row['password']==str(self.ui.le2.text())):
				self.isLoged=True
		if(self.isLoged):
			self.ui.laError.setText(u"<font color='green'> Ingresado Correctamente.")
			self.ui.ventanas.setEnabled(True)
		else:
			self.ui.laError.setText(u"<font color='red'> Usuario y/o contraseña incorrectos.")

def run():
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
