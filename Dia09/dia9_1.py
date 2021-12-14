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
        for columna in range(len(fila)):
            
            if matriz.index(fila) == 0:#Si es la primera fila:
                if (columna == 0): #Primer elemento
                    if (es_low_point(matriz,fila,columna,"sup_izq")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                elif (columna == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,columna,"sup_der")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,columna,"sup_cen")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
            
            elif matriz.index(fila) == (len(matriz)-1):#Si es la ultima fila
                if (columna == 0): #Primer elemento
                    if (es_low_point(matriz,fila,columna,"inf_izq")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                elif (columna == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,columna,"inf_der")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,columna,"inf_cen")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
            
            else:#Si es una fila normal
                if (columna == 0): #Primer elemento
                    if (es_low_point(matriz,fila,columna,"med_izq")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                elif (columna == len(fila)-1): #Ultimo elemento
                    if (es_low_point(matriz,fila,columna,"med_der")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
                else: #Elemento normal
                    if (es_low_point(matriz,fila,columna,"med_cen")):
                        listado_low_points.append(fila[columna])
                        low_points+= fila[columna] +1
    return(low_points)

def es_low_point(matriz, fila, columna, tipo):
    
    if tipo == "med_cen":
        if fila[columna] < (fila[columna-1]) and fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]) and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "med_izq":
        if fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]) and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "med_der":
        if fila[columna] < fila[columna-1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]) and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "sup_cen":
        if fila[columna] < (fila[columna-1]) and fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "sup_izq":
        if fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "sup_der":
        if fila[columna] < fila[columna-1] and fila[columna] < (matriz[matriz.index(fila)+1][columna]):
            return True
        else:
            return False
    elif tipo == "inf_cen":
        if fila[columna] < fila[columna-1] and fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]):
            return True
        else:
            return False
    elif tipo == "inf_izq":
        if fila[columna] < fila[columna+1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]):
            return True
        else:
            return False
    elif tipo == "inf_der":
        if fila[columna] < fila[columna-1] and fila[columna] < (matriz[matriz.index(fila)-1][columna]):
            return True
        else:
            return False

input_interpretada = interpretar_input(get_input())
low_points = buscar_low_points(input_interpretada)
print(low_points)
