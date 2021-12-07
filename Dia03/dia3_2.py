#Leer input
with open("input.txt") as f:
    entrada = f.readlines()
listsalida = []
for i in entrada:
   listsalida.append (i.replace("\n", ""))

#Convertir una lista de strings en matriz de caracteres
def strListToCharMatrix(str):
    listaaux =[]
    for i in listsalida:
        listaaux.append([])
        for j in i:
            listaaux[listsalida.index(i)].append(j)
    return listaaux

#Convertir lista de caracteres a enteros
def binToInt(bin):
    lstbin =[]
    for i in bin:
        lstbin.append(i)
    
    nInt = 0
    for i in range (0, len(lstbin)):
        nInt += int(lstbin[i]) * pow(2,len(lstbin)-1-i) 
    return nInt

#Obtener elementos mas comun de una matriz en la columna j
def mas_comun (lista, j):
    contar0, contar1 = 0,0
    for i in lista:
        if i[j] == "0":
            contar0 += 1
        if i[j] == "1":
            contar1 += 1
    if contar0 > contar1:
        return "0"
    else:
        return "1"

#Obtener elementos menos comun de una matriz en la columna j
def menos_comun (lista, j):
    contar0, contar1 = 0,0
    for i in lista:
        if i[j] == "0":
            contar0 += 1
        if i[j] == "1":
            contar1 += 1
    if contar0 > contar1:
        if contar1 > 0: #Tiene que haber al menos un elemeno que sea 1, si no, el menos comun es el 0
            return "1"
        else: 
            return "0"
    else:
        if contar0 > 0: #Tiene que haber al menos un elemeno que sea 0, si no, el menos comun es el 1
            return "0"
        else:
            return "1"

def get_o2 (lista, columna = 0): #Obtiene el o2, el binario cuyo elemento en cada columna sea el mas comun de la lista inicial
    new_list = []
    if (len(lista)) == 1:
        return lista[0]
    ele_mas_comun = mas_comun(lista, columna)
    for i in lista:
        if i[columna] == ele_mas_comun:
            new_list.append(i)
    return get_o2(new_list, columna+1)

def get_co2 (lista, columna = 0): #Obtiene el co2, el binario cuyo elemento en cada columna sea el menos comun de la lista inicial
    new_list = []
    if (len(lista)) == 1:
        return lista[0]
    ele_menos_comun = menos_comun(lista, columna)
    for i in lista:
        if i[columna] == ele_menos_comun:
            new_list.append(i)
    return get_co2(new_list, columna+1)


o2 = binToInt(get_o2(strListToCharMatrix(listsalida)))
co2 = binToInt(get_co2(strListToCharMatrix(listsalida)))
print(o2 * co2)
