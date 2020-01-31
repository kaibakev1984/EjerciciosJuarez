lista_nombres_provincias = ["Buenos Aires", "Córdoba", "Santa Fe" ]

"""	Se ingresan los votos por cada partido 
	ATENCIÓN: estos datos solo son para UNA provincia	"""
def cargarVotos( votos ):
	continuar = "s"
	while continuar == "s":
		partido = input("Ingresar nombre del partido: ")
		votos[ partido ] = int(input("Ingresar cantidad de votos del partido: "))
		continuar = input("Desea continuar? \"s\" para continuar: ")

"""	Recibe un diccionario "votos_por_provincia" y una lista con los nombres de cada provincia.
	Los elementos de esta lista servirán como claves para el diccionario. Se usa la función
	"cargarVotos para llenar los votos para cada provincia en particular.	"""
def cargarVotosProvincias( votos_por_provincia, lista_nombres_provincias ):
	for provincia in lista_nombres_provincias:
		print("######Conteo de votaciones en ", provincia, "######")
		votos = {}
		cargarVotos( votos )
		votos_por_provincia[ provincia ] = votos

"""	Recibe un diccionario con los votos por cada provincia, cuyo valor será un 
	diccionario con los nombres de cada partido como clave, y cantidad de votos como
	valor. Devuelve un diccionario con la suma total de todos los votos por cada
	partido	"""
def calcularVotosPorPartido( votos_por_provincia ):
	votos_por_partido = {}
	for provincia in votos_por_provincia:
		for partido in votos_por_provincia[provincia]:
			if partido not in votos_por_partido:
				votos_por_partido[partido] = votos_por_provincia[provincia][partido]
			else:
				votos_por_partido[partido] += votos_por_provincia[provincia][partido]
	return votos_por_partido
"""	Muestra todos los votos por cada partido	"""
def mostrarVotosPorPartido( votos_por_partido ):
	print("Suma total de votos por partido")
	for partido in votos_por_partido:
		print(partido, ": ", votos_por_partido[ partido ])

def main():
	votos_por_provincia = {}
	cargarVotosProvincias(votos_por_provincia, lista_nombres_provincias)
	
	votos_por_partido = calcularVotosPorPartido( votos_por_provincia )
	mostrarVotosPorPartido( votos_por_partido )

main()
