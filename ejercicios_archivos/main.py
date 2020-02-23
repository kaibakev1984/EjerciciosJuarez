def leer_MaeNov(archivo, devolver):
	linea = archivo.readline()
	if not linea:
		linea = devolver
	return linea.rstrip("\n").split(",")

def grabar_MaeActualizado(archivo, cod_art, desc_art, stock_actual):
	archivo.write(cod_art + ',' + desc_art + ',' + stock_actual + '\n')

def grabar_error(archivo, cod_art, cantidad, desc_error):
	archivo.write(cod_art + ',' + cantidad + ',' + desc_error + '\n')

def actualizar_Maestro(arMaestro, arNovedades, arMaeActualizado, arLogErrores):
	MAXIMO = "99999"
	
	cod_art_mae, desc_art, stock = leer_MaeNov(arMaestro, MAXIMO + ",,")
	cod_art_nov, cantidad_vendida = leer_MaeNov(arNovedades, MAXIMO + ",")
	
	while cod_art_mae != MAXIMO or cod_art_nov != MAXIMO:
		if cod_art_mae < cod_art_nov:
			grabar_MaeActualizado(arMaeActualizado, cod_art_mae, desc_art, str(stock))
			cod_art_mae, desc_art, stock = leer_MaeNov(arMaestro, MAXIMO + ",,")
		elif cod_art_mae > cod_art_nov:
			grabar_error(arLogErrores, cod_art_nov, cantidad_vendida, "Codigo de Articulo Inexistente en Maestro")
			cod_art_nov, cantidad_vendida = leer_MaeNov(arNovedades, MAXIMO + ",")
		else:
			if int(cantidad_vendida) <= int(stock):
				stock = int(stock) - int(cantidad_vendida)
			else:
				grabar_error(arLogErrores, cod_art_nov, cantidad_vendida, "Cantidad supera stock")
			cod_art_nov, cantidad_vendida = leer_MaeNov(arNovedades, MAXIMO + ",")

arMaestro = open("art_Maestro.csv", "r")
arNovedades = open("art_Novedades.csv", "r")
arMaeActualizado = open("art_Maestro_Actualizado.csv", "w")
arLogErrores = open("art_LogErrores.txt", "w")

print("Comienzo Proceso")

actualizar_Maestro(arMaestro, arNovedades, arMaeActualizado, arLogErrores)

print("Fin Proceso")

arMaestro.close()
arNovedades.close()
arMaeActualizado.close()
arLogErrores.close()
			
