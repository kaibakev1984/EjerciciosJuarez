def leer_archivo(archivo):
	linea = archivo.readline()
	linea = linea.rstrip('\n')
	if linea:
		return linea.split(',')
	else:
		return MAXIMO, 0 

def grabar_nuevo(archivo, cod_prod, cant_vendida):
	archivo.write(cod_prod + ',' +cant_vendida + '\n')

def mezcla_archivos(arSuc1, arSuc2, arsSucGral):
	cod_prod_s1, cant_s1 = leer_archivo(arSuc1)
	cod_prod_s2, cant_s2 = leer_archivo(arSuc2)

	while(cod_prod_s1 != MAXIMO or cod_prod_s2 != MAXIMO):

		min_cod_prod = min(cod_prod_s1 , cod_prod_s2)
		acum = 0

		while(cod_prod_s1 == min_cod_prod):
			acum += int(cant_s1)
			cod_prod_s1, cant_s1 = leer_archivo(arSuc1)

		while(cod_prod_s2 == min_cod_prod):
			acum += int(cant_s2)
			cod_prod_s2,cant_s2 = leer_archivo(arSuc2)
		cantidad = str(acum)
		grabar_nuevo(arsSucGral, min_cod_prod, cantidad)
		
######################################################################

MAXIMO = "99999"

arSuc1 = open("vtas_suc1.csv", "r")
arSuc2 = open("vtas_suc2.csv", "r")
arsSucGral = open("sucVentas.csv", "w")

mezcla_archivos(arSuc1, arSuc2, arsSucGral)

arSuc1.close()
arSuc2.close()
arsSucGral.close()


