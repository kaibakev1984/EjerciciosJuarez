################ Mezcla de VARIOS Archivos Por CLAVE MAXIMA ###################
"""Genera un unico archivo, en base a otros archivos de igual estructura
y que estan ordenados por alguno de sus datos
Cuando se encuentran dos o más "registros" con igual clave, se debe acumular el
valor de la cantidad, para DEJAR UN UNICO REGISTRO POR CLAVE EN EL NUEVO ARCHIVO."""
# Para esta solucion se utiliza el metodo de clave maxima, por el cual se define
# un valor, que nunca debe ser alcanzado por las claves que se encuentran en el
# archivo.
# Se utiliza la misma funcion de lectura para todos los archivos

def leer_Archivo(archivo):
	linea = archivo.readline()
	linea = linea.rstrip('\n')
	if not linea:
		linea = MAXIMO + ',0' #Devuelve MAXIMO y 0
	return linea.split(',')

def grabar_Nuevo(archivo, codigo_producto, cantidad_vendida):
	archivo.write(codigo_producto + ',' + cantidad_vendida + '\n')

def mezclarArchivos(arSuc1, arSuc2, arSucGral):
	cod_prod_S1, cant_S1 = leer_Archivo(arSuc1)
	cod_prod_S2, cant_S2 = leer_Archivo(arSuc2)
	
	while (cod_prod_S1 != MAXIMO or cod_prod_S2 != MAXIMO):
		min_cod_prod = min(cod_prod_S1, cod_prod_S2)
		cant_total = 0
		while (cod_prod_S1 == min_cod_prod):
			cant_total += int(cant_S1)
			cod_prod_S1, cant_S1 = leer_Archivo(arSuc1)
		while (cod_prod_S2 == min_cod_prod):
			cant_total += int(cant_S2)
			cod_prod_S2, cant_S2 = leer_Archivo(arSuc2)
		grabar_Nuevo(arSucGral, min_cod_prod, str(cant_total))
		# En caso de haber mas archivos, tendremos que agregar tantos bloques
		# while como archivos, e incorporar a la condicion del while general
		# la comparacion contra el MAXIMO
################################################################################
MAXIMO = "99999" #Valor que no debe ser alcanzado por ningun codigo de producto
arSuc1 = open("sucursal1.csv","r")
arSuc2 = open("sucursal2.csv","r")
arSucGral = open("VentasSinDuplicados.csv","w")
mezclarArchivos(arSuc1, arSuc2, arSucGral)
arSuc1.close()
arSuc2.close()
arSucGral.close()