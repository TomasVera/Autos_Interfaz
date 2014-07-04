# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Marcas.ui'
#
# Created: Fri Jul  4 13:04:35 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 395)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_nueva_marca = QtGui.QPushButton(Dialog)
        self.btn_nueva_marca.setObjectName("btn_nueva_marca")
        self.horizontalLayout.addWidget(self.btn_nueva_marca)
        self.btn_editar_marca = QtGui.QPushButton(Dialog)
        self.btn_editar_marca.setObjectName("btn_editar_marca")
        self.horizontalLayout.addWidget(self.btn_editar_marca)
        self.btn_eliminar_marca = QtGui.QPushButton(Dialog)
        self.btn_eliminar_marca.setObjectName("btn_eliminar_marca")
        self.horizontalLayout.addWidget(self.btn_eliminar_marca)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.marca_table = QtGui.QTableView(Dialog)
        self.marca_table.setObjectName("marca_table")
        self.gridLayout.addWidget(self.marca_table, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.abrir_auto2 = QtGui.QPushButton(Dialog)
        self.abrir_auto2.setObjectName("abrir_auto2")
        self.horizontalLayout_2.addWidget(self.abrir_auto2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nueva_marca.setText(QtGui.QApplication.translate("Dialog", "Nueva", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_marca.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar_marca.setText(QtGui.QApplication.translate("Dialog", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Ir a:", None, QtGui.QApplication.UnicodeUTF8))
        self.abrir_auto2.setText(QtGui.QApplication.translate("Dialog", "Autos", None, QtGui.QApplication.UnicodeUTF8))

