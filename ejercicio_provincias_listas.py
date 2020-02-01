"""	Pre:
	Se crea un diccionario llamado "votos" que usara los nombres de..
	los partidos como clave, y la cantidad de votos como valor
	Pos: Devuelve diccionario con los partidos, y la cantidad de votos
	"""
def cargarVotos():
	votos = {}
	continuar = "s"
	while(continuar):
		partido = input("Ingresar partido: ")
		votos[partido] = int(input("Ingresar cantida de votos del partido: "))
		continuar = input("Desea continuar? Presione \"enter\" para salir... ")
	return votos
"""	Se recorre las n-provincias; por cada provincia, se pide cargar los votos"""
def cargarVotosPorProvincia( cantidad_provincias ):
	votos_por_provincia = []
	for i in range(cantidad_provincias):
		print("Provincia ", i + 1)	#	i + 1 para que se muestre desde el 1
		votos_por_provincia.append(cargarVotos())
	return votos_por_provincia

"""	Pre: votos_por_provincia tiene los votos por provincia
	Se crea un diccionario de partidos, donde se acumulan los votos
	por cada provincia. Si el partido no se encuentra en dicho diccionario,
	se lo añadirá como si fuera una clave nueva; sino se acumula.
	Pos: devuelve el diccionario de partidos, con la cantidad de votos totales"""
def calcularVotosPorPartido( votos_por_provincia, cantidad_provincias ):
	votos_por_partido = {}
	for i in range(cantidad_provincias):
		for partido in votos_por_provincia[i]:
			if partido not in votos_por_partido:
				votos_por_partido[partido] = votos_por_provincia[i][partido]
			else:
				votos_por_partido[partido] += votos_por_provincia[i][partido]
	return votos_por_partido

def mostrarVotosPorPartido( votos_por_partido ):
	print("######Resultados de los votos#######")
	for partido in votos_por_partido:
		print(partido, ": ", votos_por_partido[partido])

def main():
	cantidad_provincias = 3
	votos_por_provincia = cargarVotosPorProvincia(cantidad_provincias)
	votos_por_partido = calcularVotosPorPartido( votos_por_provincia, cantidad_provincias)
	mostrarVotosPorPartido( votos_por_partido )
main()
