# -*- coding: utf-8 -*-
import sqlite3
import controller

def crearTabla():
	c = controller.conectar()
	c[0].execute('''CREATE TABLE marcas
		(id_marca INTEGER PRIMARY KEY,
		nombre TEXT,
		pais TEXT)'''
	)
	
	c[0].execute('''CREATE TABLE tipos
			(id_tipo INTEGER PRIMARY KEY,
			nombre TEXT,
			puertas INTEGER)'''
	)

	c[0].execute('''CREATE TABLE autos
			(id_auto INTEGER PRIMARY KEY,
			modelo TEXT,
			color TEXT,
			motor TEXT,
			peso INTEGER,
			descripcion TEXT,
			rendimiento INTEGER,
			imagen TEXT,
			fecha_creacion DATE,
			fk_id_tipo INTEGER,
			fk_id_marca INTEGER, FOREIGN KEY(fk_id_marca) REFERENCES marcas(id_marca))'''
	)
	 
def main():    

	crearTabla()
	
	controller.agregarInfoMarcas('Hyundai', 'Corea del Sur')
	controller.agregarInfoAutos('i10', 'Blanco', 'SOHC 1.1 cc', 1380, u'Con personalidad y estilo, el nuevo Hyundai i10 aporta una frescura nueva y mas intensidad a la conduccion.',
								18, "1.jpg", "2010", 0, 0)
	controller.agregarInfoTipos('Hatchback', 4)

	
if __name__ == '__main__':
	main()
