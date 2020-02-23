def leer_archivo(arhivo):
	linea = archivo.readline()
	if linea:
		linea.strip("\n")
	else:
		linea = ",,"	
	return linea.split(",")

def calcular_tipo(nota):
	tipo = ""
	if nota == 10:
		tipo = "S"
	elif 8 <= nota and nota < 10:
		tipo = "D"
	elif 4<= nota and nota < 8:
		tipo = "A"
	else:
		tipo = "R"
	return tipo

def escribir_archivo(archivo, archnvo):
	leg, nom, nota = leer_archivo(archivo)
	while(nota):
		nota = int(nota)
		tipo = calcular_tipo(nota)
		linea = "{},{},{}\n".format(leg,nom,tipo)
		archnvo.write(linea)
		leg, nom, nota = leer_archivo(archivo)

#################################BLOQUE PRINCIPAL#################################

archivo = open("prueba.txt","r")
archnvo = open("prueba2.txt", "w")

escribir_archivo(archivo, archnvo)
archivo.close()
archnvo.close()




