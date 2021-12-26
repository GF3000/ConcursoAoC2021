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

def suma_uno(matriz,fila,columna):
    if (matriz[fila][columna] !=0):
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
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila+1,columna+1) #diagonal
                        suma_uno(matriz, fila,columna+1)
                    elif columna == (len(matriz)-1): #Esquina superior derecha
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila+1,columna-1)
                        suma_uno(matriz, fila,columna-1) #izquierda
                    else: #Fila superior no esquina
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila+1,columna-1)
                        suma_uno(matriz, fila,columna-1) #izquierda
                        suma_uno(matriz, fila+1,columna+1) #diagonal
                        suma_uno(matriz, fila,columna+1)
                elif fila == (len(matriz)-1): #Fila inferior
                    if columna == 0: #Esquina inferior izquierda
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila-1,columna+1) #diagonal
                        suma_uno(matriz, fila,columna+1)
                    elif columna == (len(matriz)-1): #Esquina inferior derecha
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila-1,columna-1)
                        suma_uno(matriz, fila,columna-1) #izquierda
                    else: #Fila inferior no esquina
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila-1,columna-1)
                        suma_uno(matriz, fila,columna-1) #izquierda
                        suma_uno(matriz, fila-1,columna+1) #diagonal
                        suma_uno(matriz, fila,columna+1)
                else: #Fila normal
                    if columna == 0: #lateral izquierda
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila-1,columna+1) #diagonal
                        suma_uno(matriz, fila+1,columna+1) #diagonal
                        suma_uno(matriz, fila,columna+1)
                    elif columna == (len(matriz)-1): #lateral derecha
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila-1,columna-1)
                        suma_uno(matriz, fila+1,columna-1)
                        suma_uno(matriz, fila,columna-1) #izquierda
                    else: #Centrado
                        suma_uno(matriz, fila-1,columna)
                        suma_uno(matriz, fila+1,columna)#abajo
                        suma_uno(matriz, fila-1,columna+1) #diagonal
                        suma_uno(matriz, fila+1,columna+1) #diagonal
                        suma_uno(matriz, fila-1,columna-1)
                        suma_uno(matriz, fila+1,columna-1)
                        suma_uno(matriz, fila,columna+1)
                        suma_uno(matriz, fila,columna-1) #izquierda
    for cordenadas in lista_a_cero:
        matriz[cordenadas[0]][cordenadas[1]] = 0
    return veces

pasos = 0
pasos_finales = 100
contar_flashes = 0

print ("Condiciones iniciales")
for fila in entrada:
        print(fila)

while pasos < pasos_finales:
    print("\nPaso %s"%pasos)
    sumar_paso(entrada)
    print("Pre-flash")
    for fila in entrada:
        print(fila)

    suma = flashes(entrada)
    contar_flashes += suma

    suma = flashes(entrada)
    contar_flashes += suma

    suma = flashes(entrada)
    contar_flashes += suma

    suma = flashes(entrada)
    contar_flashes += suma
    
    suma = flashes(entrada)
    contar_flashes += suma
    
    suma = flashes(entrada)
    contar_flashes += suma

    suma = flashes(entrada)
    contar_flashes += suma

    suma = flashes(entrada)
    contar_flashes += suma

    print("Post-Flash")
    for fila in entrada:
        print(fila)
    pasos+=1

print("Total %s"%contar_flashes)