# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Autos.ui'
#
# Created: Fri Jul  4 13:03:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_AdministrarAutos(object):
    def setupUi(self, AdministrarAutos):
        AdministrarAutos.setObjectName("AdministrarAutos")
        AdministrarAutos.resize(752, 504)
        AdministrarAutos.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(AdministrarAutos)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_new_car = QtGui.QPushButton(AdministrarAutos)
        self.btn_new_car.setObjectName("btn_new_car")
        self.horizontalLayout_4.addWidget(self.btn_new_car)
        self.btn_edit_car = QtGui.QPushButton(AdministrarAutos)
        self.btn_edit_car.setObjectName("btn_edit_car")
        self.horizontalLayout_4.addWidget(self.btn_edit_car)
        self.btn_delete_car = QtGui.QPushButton(AdministrarAutos)
        self.btn_delete_car.setObjectName("btn_delete_car")
        self.horizontalLayout_4.addWidget(self.btn_delete_car)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(AdministrarAutos)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_buscador = QtGui.QComboBox(AdministrarAutos)
        self.cb_buscador.setObjectName("cb_buscador")
        self.horizontalLayout.addWidget(self.cb_buscador)
        self.lineEdit = QtGui.QLineEdit(AdministrarAutos)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(AdministrarAutos)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.cb_rendimiento = QtGui.QComboBox(AdministrarAutos)
        self.cb_rendimiento.setObjectName("cb_rendimiento")
        self.horizontalLayout_3.addWidget(self.cb_rendimiento)
        self.label_6 = QtGui.QLabel(AdministrarAutos)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.cb_peso = QtGui.QComboBox(AdministrarAutos)
        self.cb_peso.setObjectName("cb_peso")
        self.horizontalLayout_3.addWidget(self.cb_peso)
        self.label_7 = QtGui.QLabel(AdministrarAutos)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.cb_anio = QtGui.QComboBox(AdministrarAutos)
        self.cb_anio.setObjectName("cb_anio")
        self.horizontalLayout_3.addWidget(self.cb_anio)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.car_table = QtGui.QTableView(AdministrarAutos)
        self.car_table.setObjectName("car_table")
        self.gridLayout.addWidget(self.car_table, 3, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.imagen = QtGui.QLabel(AdministrarAutos)
        self.imagen.setObjectName("imagen")
        self.verticalLayout.addWidget(self.imagen)
        self.descripcion = QtGui.QLabel(AdministrarAutos)
        self.descripcion.setWordWrap(True)
        self.descripcion.setObjectName("descripcion")
        self.verticalLayout.addWidget(self.descripcion)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(AdministrarAutos)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.abrir_marca2 = QtGui.QPushButton(AdministrarAutos)
        self.abrir_marca2.setObjectName("abrir_marca2")
        self.horizontalLayout_2.addWidget(self.abrir_marca2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)


        marcas = [
            {"id": "0", "name": "----"},
            {"id": "1", "name": "Marca"},
            {"id": "2", "name": "Modelo"},
            {"id": "3", "name": "Motor"},
            {"id": "4", "name": "Tipo"}]
        for element in marcas:
            self.cb_buscador.addItem(element["name"], element["id"])


        index = 1
        self.cb_anio.insertItem(0, "----");
        for i in range(1920,2015):
            self.cb_anio.insertItem(index, str(i))
            index += 1


        index = 1
        self.cb_peso.insertItem(0, "----")
        for i in range(500,3001):
            self.cb_peso.insertItem(index, str(i))
            index += 1


        index = 1
        self.cb_rendimiento.insertItem(0, "--")
        for i in range(1,30):
            self.cb_rendimiento.insertItem(index, str(i))
            index += 1

        self.retranslateUi(AdministrarAutos)
        QtCore.QMetaObject.connectSlotsByName(AdministrarAutos)

    def retranslateUi(self, AdministrarAutos):
        AdministrarAutos.setWindowTitle(QtGui.QApplication.translate("AdministrarAutos", "Administrar - Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdministrarAutos", "Buscar por:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AdministrarAutos", "Rendimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AdministrarAutos", "Peso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AdministrarAutos", "Año:", None, QtGui.QApplication.UnicodeUTF8))
        self.imagen.setText(QtGui.QApplication.translate("AdministrarAutos", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion.setText(QtGui.QApplication.translate("AdministrarAutos", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AdministrarAutos", "Ir a:", None, QtGui.QApplication.UnicodeUTF8))
        self.abrir_marca2.setText(QtGui.QApplication.translate("AdministrarAutos", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
    