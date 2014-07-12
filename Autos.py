# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from Main_ui import Ui_MainWindow
import Autos_ui
import Nuevo_Auto
import Marcas

class Autos(QtGui.QDialog):
    def __init__(self):
        super(Autos, self).__init__()
        self.ui = Autos_ui.Ui_AdministrarAutos()
        self.ui.setupUi(self)
        self.show()
        self.connect_actions()

    def connect_actions(self):
        self.ui.btn_new_car.clicked.connect(self.action_btn_new_car)
        self.ui.abrir_marca2.clicked.connect(self.action_abrir_marca2)
        self.ui.btn_edit_car.clicked.connect(self.action_btn_edit_car)

    def action_btn_new_car(self):
        self.nuevoAutoWindow = Nuevo_Auto.NuevoAuto()
        self.nuevoAutoWindow.exec_()

    def action_btn_edit_car(self):
        self.nuevoAutoWindow = Nuevo_Auto.NuevoAuto()
        self.nuevoAutoWindow.exec_()

    def action_abrir_marca2(self):
        self.setVisible(False)
        self.marcasWindow = Marcas.Marcas()
        self.marcasWindow.exec_()
