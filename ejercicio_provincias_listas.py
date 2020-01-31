def cargarVotos():
	votos = {}
	continuar = "s"
	while(continuar):
		partido = input("Ingresar partido: ")
		votos[partido] = int(input("Ingresar cantida de votos del partido: "))
		continuar = input("Desea continuar? Presione \"enter\" para salir... ")
	return votos

def cargarVotosPorProvincia( cantidad_provincias ):
	votos_por_provincia = []
	for i in range(cantidad_provincias):
		print("Provincia ", i)
		votos_por_provincia.append(cargarVotos())
	return votos_por_provincia

def calcularVotosPorPartido( votos_por_provincia, cantidad_provincias ):
	votos_por_partido = {}
	for i in range(cantidad_provincias):
		for partido in votos_por_provincia[i]:
			if partido not in votos_por_partido:
				votos_por_partido[partido] = votos_por_provincia[i][partido]
			else:
				votos_por_partido[partido] += votos_por_provincia[i][partido]
	return votos_por_partido

def main():
	cantidad_provincias = 3
	votos_por_provincia = cargarVotosPorProvincia(cantidad_provincias)
	votos_por_partido = calcularVotosPorPartido( votos_por_provincia, cantidad_provincias)

main()
