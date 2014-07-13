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
        (u"Fecha", 50),
        (u"Marca", 50),
        (u"Tipo", 50)
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

    def load_data_tabla(self):
        '''Método para mostrar los datos de la tabla, muestra todos los elementos de la tabla "movies" de la base de datos'''
        datos = controller.getAutos()
        rows = len(datos)
        model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
        self.ui.car_table.setModel(model)

        for col,h in enumerate(self.tabla_columnas):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.car_table.setColumnWidth(col, h[1])

        for i,data in enumerate(datos):
            row = [data[1],data[2],data[3],data[4],data[6],data[8],data[9],data[10]]
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