# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Autos_ui
import Nuevo_Auto
import Marcas
import controller
import os

class Autos(QtGui.QDialog):
	tabla_columnas = (
		(u"Modelo",70),
		(u"Color",60),
		(u"Motor",100),
		(u"Peso", 50),
		(u"Rendimiento", 100),
		(u"Año", 50),
		(u"Tipo", 100),
		(u"Marca", 100)
		)


	def __init__(self):
		super(Autos, self).__init__()
		self.ui = Autos_ui.Ui_AdministrarAutos()
		self.ui.setupUi(self)
		self.show()
		self.connect_actions()
		self.load_data_tabla()

	def connect_actions(self):
		self.ui.btn_new_car.clicked.connect(self.action_btn_new_car)
		self.ui.abrir_marca2.clicked.connect(self.action_abrir_marca2)
		self.ui.btn_edit_car.clicked.connect(self.action_btn_edit_car)
		self.ui.btn_delete_car.clicked.connect(self.action_btn_delete_car)
		self.ui.cb_anio.currentIndexChanged[int].connect(self.indexChanged)
		self.ui.cb_peso.currentIndexChanged[int].connect(self.indexChanged)
		self.ui.cb_rendimiento.currentIndexChanged[int].connect(self.indexChanged)

	def action_btn_new_car(self):
		self.nuevoAutoWindow = Nuevo_Auto.NuevoAuto()
		self.nuevoAutoWindow.exec_()

	def action_btn_edit_car(self):
		index = self.ui.car_table.currentIndex()
		if index.row() == -1: #No se ha seleccionado producto
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage("Debe seleccionar un auto")
			return False
		else:
			id = index.row()+1
			self.nuevoAutoWindow = Nuevo_Auto.NuevoAuto(id)
			self.nuevoAutoWindow.exec_()

	def action_abrir_marca2(self):
		self.setVisible(False)
		self.marcasWindow = Marcas.Marcas()
		self.marcasWindow.exec_()

	def indexChanged(self):
		getRendimiento = int(self.ui.cb_rendimiento.currentIndex())
		if(int(self.ui.cb_peso.currentIndex())!=0):
			getPeso = int(self.ui.cb_peso.currentIndex())+499
		else:
			getPeso = 0
		if(int(self.ui.cb_anio.currentIndex())!=0):
			getAnio = int(self.ui.cb_anio.currentIndex())+1919
		else:
			getAnio = 0
		print(getRendimiento)
		print("--")
		print(getPeso)
		print("--")
		print(getAnio)
		if (getRendimiento != 0 and getPeso != 0):
			if(getAnio == 0):
				self.load_data_tabla()
			else:
				self.load_data_tabla2(getRendimiento, getAnio, getPeso)

	def load_data_tabla(self):
		datos = controller.getAutos()
		rows = len(datos)
		model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
		self.ui.car_table.setModel(model)

		for col,h in enumerate(self.tabla_columnas):
			model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
			self.ui.car_table.setColumnWidth(col, h[1])

		for i,data in enumerate(datos):
			marca = controller.getMarcaId(int(data[10]))[0]['nombre']
			tipo = controller.getTipoId(int(data[9]))[0]['nombre']
			row = [data[1],data[2],data[3],data[4],data[6],data[8],tipo,marca]
			for j, field in enumerate(row):
				index = model.index(i, j, QtCore.QModelIndex())
				model.setData(index,field)
			model.item(i).mov = data

		modelSel = self.ui.car_table.selectionModel()
		modelSel.currentChanged.connect(self.tabla_cell_selected)

	def load_data_tabla2(self, rend, anio, peso):
		datos = controller.getAutos2(rend, anio, peso)
		rows = len(datos)
		model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
		self.ui.car_table.setModel(model)

		for col,h in enumerate(self.tabla_columnas):
			model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
			self.ui.car_table.setColumnWidth(col, h[1])

		for i,data in enumerate(datos):
			marca = controller.getMarcaId(int(data[10]))[0]['nombre']
			tipo = controller.getTipoId(int(data[9]))[0]['nombre']
			row = [data[1],data[2],data[3],data[4],data[6],data[8],tipo,marca]
			for j, field in enumerate(row):
				index = model.index(i, j, QtCore.QModelIndex())
				model.setData(index,field)
			model.item(i).mov = data

		modelSel = self.ui.car_table.selectionModel()
		modelSel.currentChanged.connect(self.tabla_cell_selected)

	def tabla_cell_selected(self,index,indexp):
		id = index.row()+1
		auto = controller.getAutoId(id)
		pmap = QtGui.QPixmap(str(os.getcwd())+"/images/"+str(auto[0]['imagen']))
		self.ui.imagen.setPixmap(pmap)
		self.ui.descripcion.setText(str(auto[0]['descripcion']))

	def action_btn_delete_car(self):
		''' al clickear el boton "Eliminar"'''
		index = self.ui.car_table.currentIndex()
		if index.row() == -1: #No se ha seleccionado un producto
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage("Debe seleccionar un auto")
			return False
		else:
			msgBox1=QtGui.QMessageBox()
			msgBox1.setWindowTitle("Alerta")
			msgBox1.setText("Esta seguro? ")
			msgBox1.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			ret =msgBox1.exec_()
			if(ret==QtGui.QMessageBox.Yes):
					id = index.row()+1
					if (controller.borrarInfoAutos(id)):
						controller.borrar_imagen(id)
						self.load_data_tabla()
						msgBox = QtGui.QMessageBox()
						msgBox.setWindowTitle("Aviso")
						msgBox.setText("El producto fue eliminado con exito.")
						msgBox.exec_()
						return True
					else:
						self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
						self.ui.errorMessageDialog.showMessage("Error al eliminar el producto")
						return False