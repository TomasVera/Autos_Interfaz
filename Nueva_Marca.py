# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from MainWindow import Ui_MainWindow
import Nueva_Marca_ui

class NuevaMarca(QtGui.QDialog):
    def __init__(self):
        super(NuevaMarca, self).__init__()
        self.ui = Nueva_Marca_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()