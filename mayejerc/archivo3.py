def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	if linea:
		linea.strip("\n")
	else:
		linea = devolver
	return linea.split(",")

def escribir_arActualizado(archivo, leg, nom, sueldo):
	dato = "{}, {}, {},".format(leg, nom, sueldo)
	archivo.write(dato)

def escribir_error(archivo, leg, nom, sueldo, mensError):
	dato2 = "{}, {}, {}, {}".format(leg, nom, sueldo, mensError)
	archivo.write(dato2)

def apareo_archivos(archmae, archnov, arActualizado, archError):
	legmae, nommae, sdomae = leer_archivo(archmae, ",,")
	legnov, nomnov, sdonov, nov = leer_archivo(archnov, ",,,")

	while(legmae and legnov):
		if (legmae > legnov):
			#Agregaria los datos de arNovedades ya q no esta en el Maestro, tiene q ser un alta.
			if (nov == "A"):
				escribir_arActualizado(arActualizado, legnov, nomnov, sdonov)
				print("1")
			else:
				escribir_error(archError, legnov, nomnov, sueldonov, "El legajo no existe")
			legnov, nomnov, sdonov, nov = leer_archivo(archnov, ",,,")
		elif (legmae < legnov):
			#Copio los datos del arMaestro directamente
			escribir_arActualizado(arActualizado, legmae, nommae, sdomae)
			legmae, nommae, sdomae = leer_archivo(archmae, ",,")
			print("2")
		elif ( legmae == legnov):
			if (nov == "M"):
				escribir_arActualizado(arActualizadoct, legnov, nomnov, sdonov)
			elifco (nov == "A"):
				escribir_error(archError, legnov, nomnov, sdonov, "El legajo ya existe")
				escribir_arActualizado(arActualizadoct, legmae, nommae, sdomae)
			legmae, nommae, sdomae = leer_archivo(archmae, ",,")
			legnov, nomnov, sdonov, nov = leer_archivo(archnov, ",,,")
			print("3")

	while(legmae):
		escribir_arActualizado(arActualizado, legmae, nommae, sdomae)
		legmae, nommae, sdomae = leer_archivo(archmae, ",,")

	while(legnov):
		if(nov == "A"):
			escribir_arActualizado(arActualizado, legnov, nomnov, sdonov)
		else:
			escribir_error(archError, legnov, nomnov,sdonov, "No existe el legajo que quiere mod")
		legnov, nomnov, sdonov, nov = leer_archivo(archnov, ",,,")




#########################################Bloque Principal########################################

archmae = open("maestro.txt", "r")
archnov = open("novedades.txt", "r")
arActualizado = open("maeActualizado.txt", "w")
archError = open("arError.txt", "w")
print(apareo_archivos(archmae, archnov,arActualizado,archError))
archmae.close()
archnov.close()
arActualizado.close()
archError.close()








