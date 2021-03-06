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
		(u"Marca", 100),
		(u"id", 30)
		)


	def __init__(self):
		super(Autos, self).__init__()
		self.ui = Autos_ui.Ui_AdministrarAutos()
		self.ui.setupUi(self)
		self.show()
		self.connect_actions()
		self.load_data_tabla()


	def connect_actions(self):
                '''Metodo para conectar la accion de todos los botones'''
		self.ui.btn_new_car.clicked.connect(self.action_btn_new_car)
		self.ui.abrir_marca2.clicked.connect(self.action_abrir_marca2)
		self.ui.btn_edit_car.clicked.connect(self.action_btn_edit_car)
		self.ui.btn_delete_car.clicked.connect(self.action_btn_delete_car)
		self.ui.lineEdit.textChanged.connect(self.onChanged)
		self.ui.cb_rendimiento.currentIndexChanged[int].connect(self.indexChanged)

	def action_btn_new_car(self):
                '''Metodo para lanzar el formulario de creacion del nuevo vehiculo'''
		self.nuevoAutoWindow = Nuevo_Auto.NuevoAuto()
		self.nuevoAutoWindow.reloadT.connect(self.load_data_tabla)
		self.nuevoAutoWindow.exec_()

	def action_btn_edit_car(self):
                '''Método usado para editar un auto seleccionado desde la grilla'''
		index = self.ui.car_table.currentIndex()
		if index.row() == -1: #No se ha seleccionado producto
			msgBox = QtGui.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Debe seleccionar un auto.")
			msgBox.exec_()
			return False
		else:
			model = self.ui.car_table.model()
			id = model.index(index.row(), 8, QtCore.QModelIndex()).data()
			self.editAutoWindow = Nuevo_Auto.NuevoAuto(id)
			self.editAutoWindow.reloadT.connect(self.load_data_tabla)
			self.editAutoWindow.exec_()

	def action_abrir_marca2(self):
		self.setVisible(False)
		self.marcasWindow = Marcas.Marcas()
		self.marcasWindow.exec_()

	def indexChanged(self):
		marca = int(self.ui.cb_rendimiento.currentIndex())
		getIndex = self.ui.cb_buscador.currentIndex()
		self.load_data_tabla3(self.ui.lineEdit.text(),getIndex,marca)

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
			row = [data[1],data[2],data[3],data[4],data[6],data[8],tipo,marca,data[0]]
			for j, field in enumerate(row):
				index = model.index(i, j, QtCore.QModelIndex())
				model.setData(index,field)
			model.item(i).mov = data

		modelSel = self.ui.car_table.selectionModel()
		modelSel.currentChanged.connect(self.tabla_cell_selected)

	def load_data_tabla3(self, text, index, marca):
		datos = controller.getAutosPor(text,index,marca)
		rows = len(datos)
		model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
		self.ui.car_table.setModel(model)

		for col,h in enumerate(self.tabla_columnas):
			model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
			self.ui.car_table.setColumnWidth(col, h[1])

		for i,data in enumerate(datos):
			marca = controller.getMarcaId(int(data[10]))[0]['nombre']
			tipo = controller.getTipoId(int(data[9]))[0]['nombre']
			row = [data[1],data[2],data[3],data[4],data[6],data[8],tipo,marca,data[0]]
			for j, field in enumerate(row):
				index = model.index(i, j, QtCore.QModelIndex())
				model.setData(index,field)
			model.item(i).mov = data

		modelSel = self.ui.car_table.selectionModel()
		modelSel.currentChanged.connect(self.tabla_cell_selected)

	def tabla_cell_selected(self,index,indexp):
		model = self.ui.car_table.model()
		id = model.index(index.row(), 8, QtCore.QModelIndex()).data()
		auto = controller.getAutoId(id)
		pmap = QtGui.QPixmap(str(os.getcwd())+"/images/"+str(auto[0]['imagen']))
		pmap = pmap.scaled(250,200,QtCore.Qt.KeepAspectRatio)
		self.ui.imagen.setPixmap(pmap)
		self.ui.descripcion.setText(str(auto[0]['descripcion']))

	def action_btn_delete_car(self):
		'''Se elimina un auto directamente seleccionandolo desde la grilla con un mensaje de confirmacion"'''
		index = self.ui.car_table.currentIndex()
		if index.row() == -1: #No se ha seleccionado un producto
			msgBox = QtGui.QMessageBox()
			msgBox.setWindowTitle("Aviso")
			msgBox.setText("El auto fue eliminado con exito.")
			msgBox.exec_()
			return False
		else:
			msgBox1=QtGui.QMessageBox()
			msgBox1.setWindowTitle("Alerta")
			msgBox1.setText("Esta seguro? ")
			msgBox1.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			ret =msgBox1.exec_()
			if(ret==QtGui.QMessageBox.Yes):
					model = self.ui.car_table.model()
					id = model.index(index.row(), 8, QtCore.QModelIndex()).data()
					if (controller.borrarInfoAutos(id)):
						controller.borrar_imagen(id)
						self.load_data_tabla()
						msgBox = QtGui.QMessageBox()
						msgBox.setWindowTitle("Aviso")
						msgBox.setText("El auto fue eliminado con exito.")
						msgBox.exec_()
						return True
					else:
						self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
						self.ui.errorMessageDialog.showMessage("Error al eliminar el producto")
						return False

	def onChanged(self, text):
		'''Método para manejar el filtrado de productos por nombre, recibe el texto para filtrar y ocupa el index de la marca filtrada para obtener productos'''
		getIndex = self.ui.cb_buscador.currentIndex()
		getMarca = self.ui.cb_rendimiento.currentIndex()
		self.load_data_tabla3(text, getIndex, getMarca)
