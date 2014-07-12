# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Marcas_ui
import Nueva_Marca
import Autos
import controller

class Marcas(QtGui.QDialog):
    tabla_columnas = (
        (u"Nombre",100),
        (u"País",100),
        )

    def __init__(self):
        super(Marcas, self).__init__()
        self.ui = Marcas_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.connect_actions()
        self.load_data_tabla()

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

    def load_data_tabla(self):
        '''Método para mostrar los datos de la tabla, muestra todos los elementos de la tabla "movies" de la base de datos'''
        datos = controller.getMarcas()
        rows = len(datos)
        model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
        self.ui.marca_table.setModel(model)

        for col,h in enumerate(self.tabla_columnas):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.marca_table.setColumnWidth(col, h[1])

        for i,data in enumerate(datos):
            row = [data[1],data[2]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index,field)
            model.item(i).mov = data
