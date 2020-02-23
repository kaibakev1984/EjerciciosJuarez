class Estudiante:

	def __int__(self, nombre, leg):
		self.nombre = nombre
		self.legajo = leg

	def obtener_nombre(self):
		return self.nombre

	def obtener_legajo(self):
		return self.leg

	estudiante_cv = Estudiante("luca", 104627)
	print(obtener_nombre())
	print(obtener_legajo())