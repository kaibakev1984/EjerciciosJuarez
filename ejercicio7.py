def serie_esta_ordenada():
	a = int (input("Ingresar numero: "))
	ordenado_asc = False
	ordenado_desc = False

	#	Para continuar o salir del bucle
	continuar = "s"
	while continuar == "s":
		b = int (input("ingresar numero: "))
		if( a <= b ):
			ordenado_asc = True
		elif( a >= b ):
			ordenado_desc = True
		a = b	
		continuar = input("Desea continuar? Ingresar \'s\' para continuar... ")

	#	Se imprime un mensaje por pantalla
	if(ordenado_asc and ordenado_desc):
		print("Está desordenado")
	elif(ordenado_asc):
		print("Está ordenado ascendentemente")
	else:
		print("Está ordenado descendentemente")


print("Bienvenido al programa:")
serie_esta_ordenada()