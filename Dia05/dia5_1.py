def get_input():
    listsalida = []
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        listsalida.append (i.replace("\n", ""))
    return listsalida

def interpretar_input():
    listarectas=[]
    #Sustituir felcha por coma
    for vector in listsalida:
        listsalida[listsalida.index(vector)] = vector.replace(" -> ",",")
    #Separar por comas
    for vector in listsalida:
        listarectas.append([])
        listarectas[listsalida.index(vector)] = vector.split(",")
    #Convertir a enteros
    for vector in listarectas:
        for cordenada in vector:
            listarectas[listarectas.index(vector)][vector.index(cordenada)] = int(cordenada)

    return listarectas
    
def es_recta_horizontal(recta):
    if (recta[1] == recta[3]):#cordenadas y iguales
        return True
    else:
        return False

def es_recta_vertical(recta):
    if (recta[0] == recta[2]):#cordenadas x iguales
        return True
    else:
        return False

def puntos_por_rectas (recta):
    puntos_ocupados = []
    if(es_recta_horizontal(recta)):
        #Saber si va de izq a der o viceversa
        if (recta[0] > recta[2]):
            recta[0], recta[2] = recta[2], recta[0] #Forzamos que vaya de iquierda (el menor) a derecha (el mayor)
        longitud = recta[2] - recta[0]
        for x in range(longitud+1):#Itera por todos los puntos por los que pasa la recta
            puntos_ocupados.append([recta[0]+x, recta[1]])
    elif(es_recta_vertical(recta)):
        #Hacer que vaya de arriba a abajo
        if (recta[1] > recta [3]):
            recta[1], recta[3] = recta[3], recta[1] #Forzamos que vaya de arriba (el menor) a abajo (el mayor)
        longitud = recta[3] - recta[1]
        for y in range(longitud+1):#Itera por todos los puntos por los que pasa la recta
            puntos_ocupados.append([recta[0], recta[1]+y])
    return puntos_ocupados

def get_maximo(lista_rectas, x_o_y):
    maximo = 0
    if (x_o_y == "x"):
        for recta in lista_rectas:
            if recta[0] > maximo:
                maximo = recta[0]
            if recta[2] > maximo:
                maximo = recta[2]
    elif (x_o_y == "y"):
        for recta in lista_rectas:
            if recta[1] > maximo:
                maximo = recta[1]
            if recta[3] > maximo:
                maximo = recta[3]
    return maximo

def crear_matriz_vacia (filas, columnas):
    matriz = []
    for fila in range(filas):
        matriz.append([])
        for columna in range(columnas):
            matriz[fila].append(0)
    return matriz

def rellenar(matriz, listado):
    for recta in listado:
        puntos_a_senalizar = puntos_por_rectas(recta)
        for punto in puntos_a_senalizar:
            matriz[punto[1]-1][punto[0]-1] += 1

def contar_mayor_igual_que(matriz, n):
    veces = 0
    for fila in matriz:
        for elemento in fila:
            if elemento >= n:
                veces += 1
    return veces



listsalida= get_input()
listarectas = interpretar_input()
max_columna = get_maximo(listarectas, "x")
max_fila = get_maximo(listarectas, "y")
mapa= (crear_matriz_vacia(max_fila,max_columna))
rellenar(mapa, listarectas)
print(contar_mayor_igual_que(mapa, 2))