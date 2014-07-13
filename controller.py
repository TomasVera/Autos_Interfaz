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

def getAutos2(self, rend = None, anio = None, peso = None):
	if(anio == 0 and peso == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE rendimiento == ?"
		resultado = c.execute(query, [rend])
		datos = resultado.fetchall()
		return datos
	if(rend == 0 and peso == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE fecha_creacion == ?"
		resultado = c.execute(query, [anio])
		datos = resultado.fetchall()
		return datos
	if(rend == 0 and anio == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE peso == ?"
		resultado = c.execute(query, [peso])
		datos = resultado.fetchall()
		return datos
	if(rend == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE fecha_creacion == ? AND peso == ?"
		resultado = c.execute(query, [anio, peso])
		datos = resultado.fetchall()
		return datos
	if(anio == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE rendimiento == ? AND peso == ?"
		resultado = c.execute(query, [rend, peso])
		datos = resultado.fetchall()
		return datos	
	if(peso == 0):
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE rendimiento == ? AND fecha_creacion == ?"
		resultado = c.execute(query, [rend, anio])
		datos = resultado.fetchall()
		return datos
	else:
		c = conectar()[0]
		query = "SELECT * FROM autos WHERE rendimiento == ? AND peso == ? AND fecha_creacion == ?"
		resultado = c.execute(query, [rend, peso, anio])
		datos = resultado.fetchall()
		return datos

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