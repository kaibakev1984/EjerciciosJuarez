
"""Dado un dicc q cont cada dia del mes(clave)
[temp min del dia , temp max del dia]
escribir lasfunciones q consideren necesarias, q permita brindar la sig informacion: 
1 Listar la amplitud termica diaria (temp max - temp min)
2 Indicar cual fue la menor temp del mes y q dias ocurrio 
3 Indicar la mayor temp del mes y q dia ocurrio
4 Inf la temp max prom del mes y min"""

meses = { 
        1 : [24, 30],
        2 : [11, 28],
        3 : [20, 32],
        4 : [9, 15],
        5 : [4, 25],
        6 : [-5, 14],
        7 : [3, 12],
        8 : [-6, 25],
        9 : [15, 36],
        10 : [14, 30],
        11 : [21, 36],
        12 : [26, 38],
        }
def calcularAmplitudTermica(meses):
	amplitudTermica = {}
	for mes in meses:
		amplitudTermica[mes] = meses[mes][1] - meses[mes][0]
	return amplitudTermica
def mostrarAmplitudTermica(amplitudMeses):
	print("########## Amplitud Térmica por Meses ##########")
	for mes in amplitudMeses:
		print("Amplitud de ", mes, ": ", amplitudMeses[mes])

def mostrarTemperaturaRecord(meses, pos, mensaje):
	mes_record = 1
	for mes in meses:
		if( pos == 0 ):
			if(meses[mes_record] > meses[mes]):
				mes_record = mes
		else:
			if(meses[mes_record] < meses[mes]):
				mes_record = mes
	print(mensaje, " ocurrio en ", mes_record, " y fue de: ", meses[mes_record][pos])

def calcularPromedio(lista_temperaturas):
	acum_total = 0
	for temperatura in lista_temperaturas:
		acum_total += temperatura
	return acum_total / len(lista_temperaturas)
def calcularTemperaturaPromedio(meses):
	promedioMeses = {}
	for mes in meses:
		promedioMeses[mes] = calcularPromedio(meses[mes])
	return promedioMeses
def mostrarTemperaturaPromedio(promedioMeses):
	print("########## Temperaturas Promedio Registradas ##########")
	for mes in promedioMeses:
		print(mes, ": ", promedioMeses[mes])
def main():
	mostrarAmplitudTermica(calcularAmplitudTermica(meses))
	print("########## Temperaturas Record Registrada ##########")
	mostrarTemperaturaRecord(meses, 1, "La mayor temperatura registrada")
	mostrarTemperaturaRecord(meses, 0, "La menor temperatura registrada")
	mostrarTemperaturaPromedio(calcularTemperaturaPromedio(meses))
main()








	



    


















































 
  
   
    


