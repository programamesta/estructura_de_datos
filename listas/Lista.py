#-*- coding: utf-8 -*-
from Nodo import Nodo

class Lista(object):
	def __init__(self):
		self.nodoCabecera = None

	def listaVacia(self):
		if self.nodoCabecera == None :
			return True
		else :
			return False

	def recorrerListaHastaNull(self, nodoActual):
		if nodoActual.getSiguiente() == None:
			return nodoActual
		else:
			return self.recorrerListaHastaNull(nodoActual.getSiguiente())

	def insertarFinal(self, nombre, raza, edad):
		nuevoNodo = Nodo()
		nuevoNodo.setNombre(nombre)
		nuevoNodo.setRaza(raza)
		nuevoNodo.setEdad(edad)
		if self.listaVacia():
			self.nodoCabecera = nuevoNodo
		else :
			nodoFinal = self.recorrerListaHastaNull(self.nodoCabecera)
			nodoFinal.setSiguiente(nuevoNodo)

	def imprimirLista(self):
		contenidoLista = ""
		if self.listaVacia():
			contenidoLista = "Lista vacia"
		else :
			nodoAuxiliar = self.nodoCabecera
			while not nodoAuxiliar == None:
				contenidoLista += nodoAuxiliar.getNombre() + "\n" 
				contenidoLista += nodoAuxiliar.getRaza() + "\n" 
				contenidoLista += nodoAuxiliar.getEdad() + "\n\n"
				nodoAuxiliar = nodoAuxiliar.getSiguiente()
		print contenidoLista