# -*- coding: utf-8 -*-
import sys
import sqlite3
from PySide import QtGui, QtCore
import os

def conectar():
	con = sqlite3.connect("BASE_DATOS_PRINCIPAL.db")
	con.row_factory = sqlite3.Row
	c = [con.cursor(),con]
	return c

def getAutos():
	'''Método para obtener los autos listados en la tabla "autos"'''
	c = conectar()[0]
	query = "SELECT * FROM autos"
	resultado = c.execute(query)
	datos = resultado.fetchall()
	return datos

def getAutoId(id):
	c = conectar()[0]
	query = "SELECT * FROM autos WHERE id_auto = ?"
	resultado = c.execute(query, [id])
	auto = resultado.fetchall()
	return auto

def getMarcas():
	'''Método para obtener los autos listados en la tabla "marcas"'''
	c = conectar()[0]
	query = "SELECT * FROM marcas"
	resultado = c.execute(query)
	datos = resultado.fetchall()
	return datos

def agregarInfoMarcas(nombre, pais):
	"""
	Método que permite agregar una marca a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO marcas(nombre, pais) VALUES(?, ?)''',(nombre, pais))
	c[1].commit()

		
def agregarInfoAutos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_marca, fk_id_tipo):
	"""
	Método que permite agregar un producto a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO autos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_marca, fk_id_tipo)
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_marca, fk_id_tipo))
	c[1].commit()

def agregarInfoTipos(nombre, puertas):
	"""
	Método que permite agregar una marca a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO tipos(nombre, puertas) VALUES(?, ?)''',(nombre, puertas))
	c[1].commit()