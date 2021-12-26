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

entrada = interpretar_input(get_input())

def sumar_paso(matriz):
    for fila in range(len(matriz)):
        for columna in range (len(matriz[fila])):
            matriz[fila][columna] += 1


def flashes (matriz):
    lista_a_cero = []
    veces = 0
    for fila in range(len(matriz)):
        for columna in range (len(matriz[fila])):
            if matriz[fila][columna] >= 10 :
                lista_a_cero.append([fila, columna])
                veces +=1
                if fila == 0: #Fila superior
                    if columna == 0: #Esquina superior izquierda
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila+1][columna+1] +=1 #diagonal
                        matriz[fila][columna+1] +=1 #derecha
                    elif columna == (len(matriz)-1): #Esquina superior derecha
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila+1][columna-1] +=1 #diagonal
                        matriz[fila][columna-1] +=1 #izquierda
                    else: #Fila superior no esquina
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila+1][columna-1] +=1 #diagonal
                        matriz[fila][columna-1] +=1 #izquierda
                        matriz[fila+1][columna+1] +=1 #diagonal
                        matriz[fila][columna] +=1 #derecha
                elif fila == (len(matriz)-1): #Fila inferior
                    if columna == 0: #Esquina inferior izquierda
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila-1][columna+1] +=1 #diagonal
                        matriz[fila][columna+1] +=1 #derecha
                    elif columna == (len(matriz)-1): #Esquina inferior derecha
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila-1][columna-1] +=1 #diagonal
                        matriz[fila][columna-1] +=1 #izquierda
                    else: #Fila inferior no esquina
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila-1][columna-1] +=1 #diagonal
                        matriz[fila][columna-1] +=1 #izquierda
                        matriz[fila-1][columna+1] +=1 #diagonal
                        matriz[fila][columna] +=1 #derecha
                else: #Fila normal
                    if columna == 0: #lateral izquierda
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila-1][columna+1] +=1 #diagonal
                        matriz[fila+1][columna+1] +=1 #diagonal
                        matriz[fila][columna+1] +=1 #derecha
                    elif columna == (len(matriz)-1): #lateral derecha
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila-1][columna-1] +=1 #diagonal
                        matriz[fila+1][columna-1] +=1 #diagonal
                        matriz[fila][columna-1] +=1 #izquierda
                    else: #Centrado
                        matriz[fila-1][columna] +=1 #arriba
                        matriz[fila+1][columna] +=1 #abajo
                        matriz[fila-1][columna+1] +=1 #diagonal
                        matriz[fila+1][columna+1] +=1 #diagonal
                        matriz[fila-1][columna-1] +=1 #diagonal
                        matriz[fila+1][columna-1] +=1 #diagonal
                        matriz[fila][columna+1] +=1 #derecha
                        matriz[fila][columna-1] +=1 #izquierda
    for cordenadas in lista_a_cero:
        matriz[cordenadas[0]][cordenadas[1]] = 0
    return veces

pasos = 0
pasos_finales = 100
contar_flashes = 0
while pasos < pasos_finales:
    print("Paso %s"%pasos)
    sumar_paso(entrada)

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma
    
    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma
    
    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    suma = flashes(entrada)
    print(suma)
    contar_flashes += suma

    for fila in entrada:
        print(fila)
    pasos+=1

print("Total %s"%contar_flashes)