#Fucniones

def hay_columna(lista_bombo,matriz):
    for j in range((len(matriz[0]))):
        bool_hay_columna = True
        for i in matriz:
            if i[j] in lista_bombo:
                pass
            else:
                bool_hay_columna = False
        if bool_hay_columna:
            return True
    return False

def hay_fila (lista_bombo, matriz):
    for i in matriz:
        bool_hay_fila = True
        for j in i:
            if j in lista_bombo:
                pass
            else:
                bool_hay_fila = False
        if bool_hay_fila:
            return True
    return False


def str_to_int(string):
    listaCadena = string.split(" ")
    
    listaEnteros = []
    while "" in listaCadena:
        listaCadena.remove("")

    for i in listaCadena:
     
        listaEnteros.append(int(i))
    return listaEnteros
def sumatorio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
#Fin de funciones


with open("input.txt") as f:
    entrada = f.readlines()
listsalida = []
for i in entrada:
   listsalida.append (i.replace("\n", ""))

lista_bombo = listsalida[0].split(",")
for i in lista_bombo:
    lista_bombo[lista_bombo.index(i)] = int(i)

#lista_bombo ya ha sido obtenida

lista_tablas = listsalida.copy()
lista_tablas.remove(lista_tablas[0])

lista_matrices = [[]]
tabla = 0
for i in lista_tablas:
    if i != "":
        lista_matrices[tabla].append(i)
    else:
        lista_matrices.append([])
        tabla+=1
lista_matrices.remove(lista_matrices[0])

for matriz in lista_matrices:
    for fila in matriz:
        lista_matrices[lista_matrices.index(matriz)][matriz.index(fila)] = str_to_int(fila)

#lista_matrices ya ha sido obtenida

lista_tiempo_real = []
matrices_restantes = lista_matrices.copy()
def get_matriz_perdedor():
    
    for tiempo in range (len(lista_bombo)):
        if (len(matrices_restantes)) > 1:
            lista_tiempo_real.append(lista_bombo[tiempo])
            for matriz in matrices_restantes:
                if (hay_columna(lista_tiempo_real, matriz)):
                    matrices_restantes.remove(matriz)
                elif (hay_fila(lista_tiempo_real, matriz)):
                    matrices_restantes.remove(matriz)
    return(matrices_restantes[0])


numeros_no_marcados = []
ultima_matriz = get_matriz_perdedor()

lista_tiempo_real = []

lista_tiempo_real = []

def get_elementos_no_nulos():
    for tiempo in range (len(lista_bombo)):
        lista_tiempo_real.append(lista_bombo[tiempo])
        if (hay_columna(lista_tiempo_real, ultima_matriz)):
                #print("Hay columna en la tabla %s"%lista_matrices.index(matriz))
                return lista_matrices.index(matriz)
        if (hay_fila(lista_tiempo_real, ultima_matriz)):
                #print("Hay fila en la tabla %s"%lista_matrices.index(matriz))
                return lista_matrices.index(matriz)
                
get_elementos_no_nulos()

for fila in ultima_matriz:
    for element in fila:
        if element not in lista_tiempo_real:
            numeros_no_marcados.append(element)
print(numeros_no_marcados)
suma_elementos_no_marcados = (sumatorio(numeros_no_marcados))
ultimo_elemeto_bombo= (lista_tiempo_real[-1])
score = suma_elementos_no_marcados * ultimo_elemeto_bombo
print(score)

