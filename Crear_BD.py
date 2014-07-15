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
			fecha_creacion TEXT,
			fk_id_tipo INTEGER,
			fk_id_marca INTEGER, FOREIGN KEY(fk_id_marca) REFERENCES marcas(id_marca))'''
	)
	c[0].execute('''CREATE TABLE usuarios
			(id_user INTEGER PRIMARY KEY,
			username TEXT,
			password TEXT)'''
	)
	 
def main():    

	crearTabla()
	
	controller.agregarInfoUsuarios('Molina', '1234')
	controller.agregarInfoUsuarios('Felipe', '1234')
	controller.agregarInfoUsuarios('Jaime', '1234')
	controller.agregarInfoUsuarios('Tomas', '1234')

	controller.agregarInfoMarcas('Hyundai', 'Corea del Sur')
	controller.agregarInfoMarcas('Suzuki', 'Japon')
	controller.agregarInfoMarcas('Nissan', 'Japon')
	controller.agregarInfoTipos('Hatchback', 5)
	controller.agregarInfoTipos('Sedan', 5)
	controller.agregarInfoAutos('i10', 'Blanco', '1.1 Lts', 1380, u'Con personalidad y estilo, el nuevo Hyundai i10 aporta una frescura nueva y mas intensidad a la conduccion.',
								18, "1.jpg", "2010", 1, 1)
	controller.agregarInfoAutos('Sonata', 'Negro', '2.0 Lts', 1850, u'Suave y comodo al conducir ademas de insonoridad en el habitaculo',
								11, "2.jpg", "2012", 2, 1)
	controller.agregarInfoAutos('Maruti', 'Blanco', '0.8 Lts', 780, u'Preferencialmente auto para uso urbano, destaca su agilidad y su rendimiento',
								21, "3.jpg", "2009", 1, 2)
	controller.agregarInfoAutos('Alto K10', 'Rojo', '1.0 Lts', 890, u'Uso preferencialmente urbano, buena aceleracion a partir de la inercia, buena maneobralidad y buen rendimiento',
								20, "4.jpg", "2013", 1, 2)
	controller.agregarInfoAutos('Sentra', 'Gris', '2.0 Lts', 1590, u'Destaca su comodidad al conducir ademas de su suavidad, principalmente insonoro en autopista.',
								15, "5.jpg", "2011", 2, 3)
	


	
if __name__ == '__main__':
	main()
