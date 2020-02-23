
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

"""def temp_prom(meses): #una manera de hacerlo sin modularizar
    sumatoria = 0
    cont = 0
    for i in meses:
        sumatoria += meses[i][0]
        cont+= 1
    return sumatoria/cont

def main():
    print(temp_prom(meses))
main()"""

def temperaturas_promedio_anual(meses, pos):
    sumatoria = 0
    for mes in meses:
        sumatoria += meses[mes][pos]
    return sumatoria/len(meses)

def temp_ext_promedio_mensual(meses):
	for mes in meses:
		#sumatoria = meses[mes][0] + meses[mes][1]  Ambos hacen lo mismo
		#sumatoria = sum(meses[mes])     
		#print("Temperatura promedio del mes:",sumatoria/len(meses))
		print("Temperatura promedio del mes:",sum(meses[mes])/len(meses))

def listar_amplitud_termica(meses):
    amplitud = 0
    for mes in meses:
        amplitud = meses[mes][1] - meses[mes][0]
        print("Amplitud termica en el mes:", mes, "=",amplitud)
    return amplitud

def temp_minima(meses, pos):
	mes_frio = 1
	temp_min = meses[1][pos]
	for mes in meses:
		if meses[mes][pos] < temp_min:
			mes_frio = mes #solo guardo la clave para saber el mes
			temp_min = meses[mes][pos]
	return mes_frio, temp_min

def temp_maxima(meses, pos):
	mes_ocurrido = 1
	temp_max = meses[1][pos]
	for mes in meses:
		if meses[mes][pos] > temp_max:
			mes_ocurrido = mes #solo guardo la clave para saber el mes
			temp_max = meses[mes][pos] #guardo el valor en esa posicion
	return mes_ocurrido, temp_max
    
def main():
    print("Minimo promedio anual: ", temperaturas_promedio_anual(meses, 0))
    print("Máximo promedio anual: ", temperaturas_promedio_anual(meses, 1))
    amplitud = ( listar_amplitud_termica(meses))
    mes_frio, temp_min = temp_minima(meses, 0)
    mes_calid, temp_max = temp_maxima(meses, 1)
    temp_ext_promedio_mensual(meses)
    print("La temp min fue en el mes: ",mes_frio,"temp min: ", temp_min)
    print("La temp maxima fue en el mes:",mes_calid,"con:", temp_max)
main()

