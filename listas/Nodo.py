#-*- coding: utf-8 -*-

class Nodo(object):

	def __init__(self):
		self.nombre = None
		self.raza = None
		self.edad = None
		self.siguiente = None

	def setNombre(self, _nombre):
	 	self.nombre = _nombre

	def setRaza(self, _raza):
	 	self.raza = _raza

	def setEdad(self, _edad):
	 	self.edad = _edad

	def setSiguiente(self, _siguiente):
		self.siguiente = _siguiente

	def getNombre(self):
		return self.nombre

	def getSiguiente(self):
		return self.siguiente

	def getRaza(self):
		return self.raza

	def getEdad(self):
		return self.edad
		