# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import Nuevo_Auto_ui

class NuevoAuto(QtGui.QDialog):
    def __init__(self):
        super(NuevoAuto, self).__init__()
        self.ui = Nuevo_Auto_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
