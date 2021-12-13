from typing import Tuple


def get_input():
    
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        entrada[entrada.index(i)] = i.replace("\n", "")
    
    return entrada

def interpretar_input(input):
    input_interpretada = []
    for fila in input:
        input_interpretada.append([])
        for numero in fila:
            input_interpretada[input.index(fila)].append(int(numero))
    return input_interpretada
listado_low_points = []
def buscar_low_points(matriz):
    low_points = 0
    
    for fila in matriz:
        for numero in fila:
            
            if matriz.index(fila) == 0:#Si es la primera fila:
                if (fila.index(numero) == 0): #Primer elemento
                    if (es_low_point(matriz,fila,numero,"sup_izq")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                elif (fila.index(numero) == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,numero,"sup_der")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,numero,"sup_cen")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
            
            elif matriz.index(fila) == (len(matriz)-1):#Si es la ultima fila
                if (fila.index(numero) == 0): #Primer elemento
                    if (es_low_point(matriz,fila,numero,"inf_izq")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                elif (fila.index(numero) == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,numero,"inf_der")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,numero,"inf_cen")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
            
            else:#Si es una fila normal
                if (fila.index(numero) == 0): #Primer elemento
                    if (es_low_point(matriz,fila,numero,"med_izq")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                elif (fila.index(numero) == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,numero,"med_der")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,numero,"med_cen")):
                        listado_low_points.append(numero)
                        low_points+= numero +1
    return(low_points)

def es_low_point(matriz, fila, numero, tipo):
    
    if tipo == "med_cen":
        if numero < (fila[fila.index(numero)-1]) and numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]) and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "med_izq":
        if numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]) and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "med_der":
        if numero < fila[fila.index(numero)-1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]) and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "sup_cen":
        if numero < (fila[fila.index(numero)-1]) and numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "sup_izq":
        if numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "sup_der":
        if numero < fila[fila.index(numero)-1] and numero < (matriz[matriz.index(fila)+1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "inf_cen":
        if numero < fila[fila.index(numero)-1] and numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "inf_izq":
        if numero < fila[fila.index(numero)+1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]):
            return True
        else:
            return False
    elif tipo == "inf_der":
        if numero < fila[fila.index(numero)-1] and numero < (matriz[matriz.index(fila)-1][fila.index(numero)]):
            return True
        else:
            return False

input_interpretada = interpretar_input(get_input())
# low_points = buscar_low_points(input_interpretada)
# print(listado_low_points)
# print(low_points)
print(input_interpretada[12][44])