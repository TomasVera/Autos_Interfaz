# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Nueva_Marca_ui
import controller

class NuevaMarca(QtGui.QDialog):
	reloadT = QtCore.Signal()
	identificador = False
	change_image = False
	def __init__(self, id=None):
		super(NuevaMarca, self).__init__()
		self.ui = Nueva_Marca_ui.Ui_Dialog()
		self.ui.setupUi(self)
		self.show()
		if(id==None):
			self.id=0
			self.identificador = False
			self.setWindowTitle("Nueva Marca")
			self.show()
		else:
			self.id=id
			self.identificador = True
			self.setWindowTitle("Editar Marca")
			auto = controller.getMarcaId(id)
			for row in auto:
				self.ui.nombre_marca.setText(row['nombre'])
				self.ui.pais_marca.setText(row['pais'])
		self.accepted.connect(self.action_btn_aceptar)

	def action_btn_aceptar(self):
		nombre = str(self.ui.nombre_marca.text())
		pais = str(self.ui.pais_marca.text())
		if self.identificador == False:
			controller.agregarInfoMarcas(nombre, pais)  
		else:
			controller.editarInfoMarcas(self.id, nombre, pais)  
		self.setVisible(False)
		self.reloadT.emit()
