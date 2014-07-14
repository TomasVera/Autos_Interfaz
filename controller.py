# -*- coding: utf-8 -*-
import sys
import sqlite3
from PySide import QtGui, QtCore
import os
import shutil

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

def getAutos2(rend, anio, peso):
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
		anio = str(anio)
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

def getMarcaId(id):
	c = conectar()[0]
	query = "SELECT * FROM marcas WHERE id_marca = ?"
	resultado = c.execute(query, [id])
	auto = resultado.fetchall()
	return auto

def getTipos():
	'''Método para obtener los tipo listados en la tabla "tipos"'''
	c = conectar()[0]
	query = "SELECT * FROM tipos"
	resultado = c.execute(query)
	datos = resultado.fetchall()
	return datos

def getTipoId(id):
	c = conectar()[0]
	query = "SELECT * FROM tipos WHERE id_tipo = ?"
	resultado = c.execute(query, [id])
	auto = resultado.fetchall()
	return auto

def agregarInfoMarcas(nombre, pais):
	"""
	Método que permite agregar una marca a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO marcas(nombre, pais) VALUES(?, ?)''',(nombre, pais))
	c[1].commit()

		
def agregarInfoAutos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca):
	"""
	Método que permite agregar un auto a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO autos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca)
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca))
	c[1].commit()

def editarInfoAutos(id, modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca):
	"""
	Método que permite editar un auto en la base de datos
	"""
	c = conectar()
	query = "UPDATE autos SET modelo = ?,color = ?, motor = ?, peso = ?, descripcion = ?, rendimiento = ?, imagen = ?, fecha_creacion = ?, fk_id_tipo = ?, fk_id_marca = ? WHERE id_auto = ?"
	c[0].execute(query, [modelo,color,motor,peso,descripcion,rendimiento,imagen,fecha_creacion,fk_id_tipo,fk_id_marca,id])
	c[1].commit()

def editarInfoMarcas(id, nombre, pais):
	"""
	Método que permite editar un auto en la base de datos
	"""
	c = conectar()
	query = "UPDATE marcas SET nombre = ?,pais = ? WHERE id_marca = ?"
	c[0].execute(query, [nombre, pais, id])
	c[1].commit()

def borrarInfoAutos(id):
	"""
	Método para borrar un auto directo en la base de datos, requiere la id del auto seleccionado para borrar
	"""
	c = conectar()
	exito = False
	query = "DELETE FROM autos WHERE id_auto = ?"
	try:
		resultado = c[0].execute(query, [id])
		c[1].commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	return exito

def borrarInfoAutosMarca(id_marca):
	"""
	Método para borrar un auto directo en la base de datos, requiere la marca del auto seleccionado para borrar
	"""
	c = conectar()
	exito = False
	query = "DELETE FROM autos WHERE fk_id_marca = ?"
	try:
		resultado = c[0].execute(query, [id_marca])
		c[1].commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	return exito

def borrarInfoMarcas(id):
	"""
	Método para borrar un auto directo en la base de datos, requiere la id del auto seleccionado para borrar
	"""
	c = conectar()
	exito = False
	query = "DELETE FROM marcas WHERE id_marca = ?"
	try:
		id_marca = getMarcaId(id)[0]['id_marca']
		borrarInfoAutosMarca(id_marca)
		resultado = c[0].execute(query, [id])
		c[1].commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	return exito

def agregarInfoTipos(nombre, puertas):
	"""
	Método que permite agregar un tipo a la base de datos
	"""
	c = conectar()
	c[0].execute('''INSERT INTO tipos(nombre, puertas) VALUES(?, ?)''',(nombre, puertas))
	c[1].commit()



def guardar_imagen(image_filename,image):
	'''Método que genera una copia del archivo 'image_filename' que guarda en el direcctorio del programa'''
	try:
		os.mkdir(str(os.getcwd())+'/images')
	except:
		pass
	shutil.copy(image_filename, str(os.getcwd())+'/images/'+image)

def borrar_imagen(id):
	'''Método que elimina un fichero generado por el método "guardar_imagen"'''
	if(buscar_imagen(id)):
		os.remove(str(os.getcwd())+'/images/'+str(id)+'.jpg')

def buscar_imagen(id):
	'''Método que busca en el directorio del programa la imagen de un determinado auto(por su id), retorna 'True' si existe y 'False' si no''' 
	if(os.path.exists(str(os.getcwd())+'/images/'+str(id)+'.jpg')):
		return True
	else:
		return False