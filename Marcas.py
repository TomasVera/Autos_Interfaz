# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from Main_ui import Ui_MainWindow
import Marcas_ui
import Nueva_Marca
import Autos

class Marcas(QtGui.QDialog):
    def __init__(self):
        super(Marcas, self).__init__()
        self.ui = Marcas_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.connect_actions()

    def connect_actions(self):
        self.ui.btn_nueva_marca.clicked.connect(self.action_btn_nueva_marca)
        self.ui.abrir_auto2.clicked.connect(self.action_abrir_auto2)
        self.ui.btn_editar_marca.clicked.connect(self.action_btn_editar_marca)

    def action_btn_nueva_marca(self):
        self.nuevaMarcaWindow = Nueva_Marca.NuevaMarca()
        self.nuevaMarcaWindow.exec_()

    def action_btn_editar_marca(self):
        self.nuevaMarcaWindow = Nueva_Marca.NuevaMarca()
        self.nuevaMarcaWindow.exec_()

    def action_abrir_auto2(self):
        self.setVisible(False)
        self.autosWindow = Autos.Autos()
        self.autosWindow.exec_()
