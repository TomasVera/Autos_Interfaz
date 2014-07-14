# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Autos_ui.ui'
#
# Created: Mon Jul 14 01:59:29 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import controller
class Ui_AdministrarAutos(object):
    def setupUi(self, AdministrarAutos):
        AdministrarAutos.setObjectName("AdministrarAutos")
        AdministrarAutos.resize(930, 531)
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
        self.car_table = QtGui.QTableView(AdministrarAutos)
        self.car_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.car_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.car_table.setObjectName("car_table")
        self.gridLayout.addWidget(self.car_table, 4, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.imagen = QtGui.QLabel(AdministrarAutos)
        self.imagen.setMinimumSize(QtCore.QSize(250, 200))
        self.imagen.setMaximumSize(QtCore.QSize(250, 200))
        self.imagen.setObjectName("imagen")
        self.verticalLayout.addWidget(self.imagen)
        self.descripcion = QtGui.QLabel(AdministrarAutos)
        self.descripcion.setMinimumSize(QtCore.QSize(250, 200))
        self.descripcion.setMaximumSize(QtCore.QSize(250, 200))
        self.descripcion.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descripcion.setWordWrap(True)
        self.descripcion.setObjectName("descripcion")
        self.verticalLayout.addWidget(self.descripcion)
        self.gridLayout.addLayout(self.verticalLayout, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(AdministrarAutos)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.abrir_marca2 = QtGui.QPushButton(AdministrarAutos)
        self.abrir_marca2.setObjectName("abrir_marca2")
        self.horizontalLayout_2.addWidget(self.abrir_marca2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(AdministrarAutos)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.cb_rendimiento = QtGui.QComboBox(AdministrarAutos)
        self.cb_rendimiento.setObjectName("cb_rendimiento")
        self.horizontalLayout_3.addWidget(self.cb_rendimiento)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        marcas = [
            {"id": "0", "name": "----"},
            {"id": "1", "name": "Modelo"},
            {"id": "2", "name": "Color"},
            {"id": "3", "name": "Motor"},
            {"id": "4", "name": "Peso"},
            {"id": "5", "name": u"Año"},
            {"id": "6", "name": "Rendimiento"},
            {"id": "7", "name": "Tipo"}]
        for element in marcas:
            self.cb_buscador.addItem(element["name"], element["id"])

        datos = controller.getMarcas()
        self.marcas = [{"id": "0", "name": "----"}]
        for i in datos:
            actual = {"id": str(i['id_marca']), "name":str(i['nombre'])}
            self.marcas.append(actual)

        for element in self.marcas:
            self.cb_rendimiento.addItem(element["name"], element["id"])

        self.retranslateUi(AdministrarAutos)
        QtCore.QMetaObject.connectSlotsByName(AdministrarAutos)

    def retranslateUi(self, AdministrarAutos):
        AdministrarAutos.setWindowTitle(QtGui.QApplication.translate("AdministrarAutos", "Administrar - Autos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete_car.setText(QtGui.QApplication.translate("AdministrarAutos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.imagen.setText(QtGui.QApplication.translate("AdministrarAutos", "[Imagen]", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion.setText(QtGui.QApplication.translate("AdministrarAutos", "[Descripcion]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AdministrarAutos", "Ir a:", None, QtGui.QApplication.UnicodeUTF8))
        self.abrir_marca2.setText(QtGui.QApplication.translate("AdministrarAutos", "Marcas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AdministrarAutos", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdministrarAutos", "Buscar por:", None, QtGui.QApplication.UnicodeUTF8))

