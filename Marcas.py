# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Marcas_ui
import Nueva_Marca
import Autos
import controller

class Marcas(QtGui.QDialog):
    tabla_columnas = (
        (u"Nombre",147),
        (u"País",146),
        (u"Total Autos",100),
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
        self.ui.btn_eliminar_marca.clicked.connect(self.action_btn_eliminar_marca)

    def action_btn_nueva_marca(self):
        self.nuevaMarcaWindow = Nueva_Marca.NuevaMarca()
        self.nuevaMarcaWindow.reloadT.connect(self.load_data_tabla)
        self.nuevaMarcaWindow.exec_()

    def action_btn_editar_marca(self):
        '''Metodo para editar una marca seleccionandola desde la grilla'''
        index = self.ui.marca_table.currentIndex()
        if index.row() == -1: #No se ha seleccionado producto
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una marca")
            return False
        else:
            id = index.row()+1
            self.editMarcaWindow = Nueva_Marca.NuevaMarca(id)
            self.editMarcaWindow.reloadT.connect(self.load_data_tabla)
            self.editMarcaWindow.exec_()

    def action_abrir_auto2(self):
        self.setVisible(False)
        self.autosWindow = Autos.Autos()
        self.autosWindow.exec_()

    def load_data_tabla(self):
        '''Método para mostrar los datos de la tabla, muestra todos los elementos de la tabla Marcas de la base de datos'''
        datos = controller.getMarcas()
        rows = len(datos)
        model = QtGui.QStandardItemModel(rows,len(self.tabla_columnas))
        self.ui.marca_table.setModel(model)

        for col,h in enumerate(self.tabla_columnas):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.marca_table.setColumnWidth(col, h[1])

        for i,data in enumerate(datos):
            autos = controller.getAutos()
            total=0
            for row in autos:
                if(data[0]==row['fk_id_marca']):
                    total=total+1
            row = [data[1],data[2],total]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index,field)
            model.item(i).mov = data

    def action_btn_eliminar_marca(self):
        '''Metodo que elimina una Marca '''
        index = self.ui.marca_table.currentIndex()
        if index.row() == -1: #No se ha seleccionado un producto
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una marca")
            return False
        else:
            msgBox1=QtGui.QMessageBox()
            msgBox1.setWindowTitle("Alerta")
            msgBox1.setText("Esta seguro? ")
            msgBox1.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            ret =msgBox1.exec_()
            if(ret==QtGui.QMessageBox.Yes):
                    id = index.row()+1
                    if (controller.borrarInfoMarcas(id)):
                        self.load_data_tabla()
                        msgBox = QtGui.QMessageBox()
                        msgBox.setWindowTitle("Aviso")
                        msgBox.setText("La marca fue eliminada con exito.")
                        msgBox.exec_()
                        return True
                    else:
                        self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                        self.ui.errorMessageDialog.showMessage("Error al eliminar el producto")
                        return False
