# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import string
import os


def validaDatos(modelo, color, motor, peso, descripcion,rendimiento, imagen, fecha_creacion):
                '''Valida cada uno de los datos que se ingresan y devuelve una cadena string con los errores
                   que tiene cada campo'''
                validModelo=validaTexto(modelo, 'no_simbolos')
                validColor=validaTexto(color, 'texto')
                validMotor=validaTexto(motor, 'no_simbolos')
                validPeso=validaTexto(peso, 'numeros')
                validDescripcion=validaTexto(descripcion, 'no_simbolos')
                validRendimiento=validaTexto(rendimiento, 'numeros')
                validaImagen=True
                validafecha=True
                error="Campos Incorrectos:"
                if(validModelo==False):
                                mod="*Modelo"
                                error=error+mod
                if(validColor==False):
                                coolor="*Color"
                                error=error+"  "+coolor
                if(validMotor==False):
                                mot="*Motor"
                                error=error+"   "+mot
                if(validPeso==False):
                                pes="*Peso"
                                error=error+"  "+pes
                if(validDescripcion==False):
                                description="*Descripcion"
                                error=error+"   "+description
                if(validRendimiento==False):
                                rend="*Rendimiento"
                                error=error+" "+rend
                return error
        

                

def validaTexto(text,validacion):
	'''Función que evalua y valida el string 'text' dependiendo el valor del segundo parámetro:
	numeros: retorna 'True' si el string 'text' posee sólo numeros
	no_simbolos: retorna 'True' si el string 'text' posee sólo letras (mayusculas o minusculas o acentos) y/o números
	Retorna 'False' en caso contrario o si el string 'text' esta vacío'''

	Valido=True

	if (validacion=="numeros"):
		Cadena = "0123456789"

	if (validacion=="no_simbolos"):
		Cadena = " ,.-abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789"

	if (validacion=="texto"):
		Cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"

	i=0
	StringNum=str(text)

	if(len(StringNum)==0):
		Valido=False

	while(Valido and (i<len(StringNum))):
		if (not StringNum[i] in Cadena):
			Valido=False
		i=i+1
	return Valido



