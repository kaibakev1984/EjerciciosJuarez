# Listar archivo elemento a elemento, separando cada uno de los datos
# que vinen en la línea e informando al final el total general de
# cantidad y de importe

def listar_archivo():
	with open("ventas.csv", "r") as arVentas:
		total_cant = 0
		importe = 0
		for linea in arVentas:
			suc, codigo, stock, precio = linea.rstrip('\n').split(',')
			print(suc, codigo, stock, precio)
			total_cant += int(stock)
			importe += int(precio)
		print(total_cant, importe)

listar_archivo()
			
