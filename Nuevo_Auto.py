# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Nuevo_Auto_ui
import controller
import os

class NuevoAuto(QtGui.QDialog):
	identificador = False
	change_image = False
	def __init__(self, id=None):
		super(NuevoAuto, self).__init__()
		self.ui = Nuevo_Auto_ui.Ui_Dialog()
		self.ui.setupUi(self)
		self.show()
		self.connect_actions()
		if(id==None):
			self.identificador = False
			self.setWindowTitle("Nuevo Auto")
			self.show()

		else:
			self.identificador = True
			self.setWindowTitle("Editar Auto")
			auto = controller.getAutoId(id)
			for row in auto:
				self.ui.modelo_auto.setText(row['modelo'])
				self.ui.color_auto.setText(row['color'])
				self.ui.motor_auto.setText(row['motor'])
				#self.ui.tipo_auto.setText(row['tipo'])
				self.ui.edit_descripcion.setText(row['descripcion'])
				self.ui.rendimiento_auto.setText(str(row['rendimiento']))
				self.ui.peso_auto.setText(str(row['peso']))
				self.ui.marca_auto.setCurrentIndex(int(row['fk_id_marca']))
			if(auto[0]['imagen']!=None):
				pmap = QtGui.QPixmap(str(os.getcwd())+"/images/"+str(auto[0]['imagen']))
				self.ui.nueva_imagen.setPixmap(pmap)
			else:
				self.ui.nueva_imagen.setText("<font color='red'> Producto sin imagen")

	def connect_actions(self):
		self.ui.btn_examinar.clicked.connect(self.action_btn_examinar)
		self.accepted.connect(self.action_btn_aceptar)

	def action_btn_examinar(self):
		self.ex = QtGui.QFileDialog()
		data = self.ex.getOpenFileName()
		image_filename = data[0]
		image_ext = str(os.path.splitext(image_filename)[1])
		if(image_filename):
			self.image_filename = image_filename
			if(image_ext==".jpg"):
				pmap = self.image_filename
				self.ui.nueva_imagen.setPixmap(pmap)
				self.change_image = True
			elif(image_ext):
				msgBox = QtGui.QMessageBox()
				msgBox.setWindowTitle("ERROR")
				msgBox.setText("Formato de archivo no soportado.")
				msgBox.exec_()

	def action_btn_aceptar(self):
		if self.identificador == False:
			modelo = str(self.ui.modelo_auto.text())
			color = str(self.ui.color_auto.text())
			motor = str(self.ui.motor_auto.text())
			descripcion = str(self.ui.edit_descripcion.toPlainText())
			rendimiento = int(self.ui.rendimiento_auto.text())
			peso = int(self.ui.peso_auto.text())
			imagen = self.image_filename
			fecha_creacion = 0
			fk_id_marca = 1
			fk_id_tipo = 1
			print imagen
			controller.agregarInfoAutos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_marca, fk_id_tipo)  
			self.setVisible(False)
		#else:
			

		#if(self.change_image):
		#	controller.guardar_imagen(self.image_filename,"0.jpg")
