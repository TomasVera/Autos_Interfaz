# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nuevo_Auto.ui'
#
# Created: Fri Jul  4 13:05:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 423)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.marca_auto = QtGui.QLineEdit(Dialog)
        self.marca_auto.setObjectName("marca_auto")
        self.verticalLayout_4.addWidget(self.marca_auto)
        self.peso_auto = QtGui.QLineEdit(Dialog)
        self.peso_auto.setObjectName("peso_auto")
        self.verticalLayout_4.addWidget(self.peso_auto)
        self.rendimiento_auto = QtGui.QLineEdit(Dialog)
        self.rendimiento_auto.setObjectName("rendimiento_auto")
        self.verticalLayout_4.addWidget(self.rendimiento_auto)
        self.cb_creacion_auto = QtGui.QComboBox(Dialog)
        self.cb_creacion_auto.setMouseTracking(False)
        self.cb_creacion_auto.setObjectName("cb_creacion_auto")
        self.verticalLayout_4.addWidget(self.cb_creacion_auto)
        self.sb_n_puertas = QtGui.QSpinBox(Dialog)
        self.sb_n_puertas.setObjectName("sb_n_puertas")
        self.verticalLayout_4.addWidget(self.sb_n_puertas)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.edit_descripcion = QtGui.QTextEdit(Dialog)
        self.edit_descripcion.setObjectName("edit_descripcion")
        self.verticalLayout_6.addWidget(self.edit_descripcion)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.modelo_auto = QtGui.QLineEdit(Dialog)
        self.modelo_auto.setObjectName("modelo_auto")
        self.verticalLayout_3.addWidget(self.modelo_auto)
        self.color_auto = QtGui.QLineEdit(Dialog)
        self.color_auto.setObjectName("color_auto")
        self.verticalLayout_3.addWidget(self.color_auto)
        self.motor_auto = QtGui.QLineEdit(Dialog)
        self.motor_auto.setObjectName("motor_auto")
        self.verticalLayout_3.addWidget(self.motor_auto)
        self.tipo_auto = QtGui.QLineEdit(Dialog)
        self.tipo_auto.setObjectName("tipo_auto")
        self.verticalLayout_3.addWidget(self.tipo_auto)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.nueva_imagen = QtGui.QLabel(Dialog)
        self.nueva_imagen.setObjectName("nueva_imagen")
        self.verticalLayout_5.addWidget(self.nueva_imagen)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_examinar = QtGui.QPushButton(Dialog)
        self.btn_examinar.setObjectName("btn_examinar")
        self.horizontalLayout.addWidget(self.btn_examinar)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Peso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Rendimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Año creacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "N° Puertas:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Modelo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Motor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Tipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Imagen:", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_imagen.setText(QtGui.QApplication.translate("Dialog", "Aqui va la imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_examinar.setText(QtGui.QApplication.translate("Dialog", "Examinar", None, QtGui.QApplication.UnicodeUTF8))
