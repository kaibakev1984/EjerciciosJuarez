# Genera un maestro actualizado, en base al archivo maestro original y las
# novedades que vienen informadas en el archivo de novedades.
# En este caso, en el archivo de Novedades, pueden venir registros duplicados.

MAXIMA = "9999"

def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	linea = linea.rstrip("\n")
	if not linea:
		linea = devolver
	return linea.split(",")

def grabar_archActualizado(archivo, cod_art, descripcion, stock_art):
	datos = "{}, {}, {}\n".format(cod_art, descripcion, stock_art)
	archivo.write(datos)

def grabar_arError(archivo, cod_art, stock_art, mensError):
	datos = "{}, {}, {}\n".format(cod_art, stock_art, mensError)
	archivo.write(datos)

def Apareo_clave_max(arMaestro, arNovedades, arActualizado, arError):

	cod_art_mae, desc_art, stock_art_mae = leer_archivo(arMaestro, MAXIMA+",,")
	cod_art_nov, stock_art_nov = leer_archivo(arNovedades, MAXIMA+",")

	while(cod_art_mae != MAXIMA or cod_art_nov != MAXIMA):
		if (cod_art_mae < cod_art_nov):
			grabar_archActualizado(arActualizado, cod_art_mae, desc_art, stock_art_mae)
			cod_art_mae, desc_art, stock_art_mae = leer_archivo(arMaestro, MAXIMA+",,")
		elif(cod_art_nov < cod_art_mae):
			grabar_arError(arError, cod_art_nov, stock_art_nov, "No existe el articulo")
			cod_art_nov, stock_art_nov = leer_archivo(arNovedades, MAXIMA+",")
		else:
			if (int(stock_art_mae) >= int(stock_art_nov)):
				stock_art_mae = int(stock_art_mae) - int(stock_art_nov)
				grabar_archActualizado(arActualizado, cod_art_nov, desc_art, stock_art_mae)
			else: 
				grabar_arError(arError, cod_art_nov, stock_art_nov, "Fuera de stock")
			#No se leen los 2 x si hay otra novedad del mismo articulo, solo se lee arNov
			
			cod_art_nov, stock_art_nov = leer_archivo(arNovedades, MAXIMA+",")

#######################################Bloque Principal############################################

arMaestro = open("art_Maestro.csv", "r")
arNovedades = open("art_Novedades.csv", "r")
arActualizado = open("art_Actualizado.csv", "w")
arError = open("art_Error.csv", "w")

Apareo_clave_max(arMaestro, arNovedades, arActualizado, arError)

arMaestro.close()
arNovedades.close()
arActualizado.close()
arError.close()




