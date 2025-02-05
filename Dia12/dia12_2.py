def get_input():
    
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        entrada[entrada.index(i)] = i.replace("\n", "")
    
    return entrada

def interpretar_input(input):
    input_interpretada = []
    for dupla in input:
        aux = dupla.split("-")
        input_interpretada.append([aux[0], aux[1]])    
    return input_interpretada


def crear_diccionarios(entrada):
    comunicaciones = {}
    for dupla_main in entrada:
        for elemento in dupla_main:
            comunicaciones[elemento] = []
            for dupla_aux in entrada:
                if dupla_aux[1] == elemento:
                    comunicaciones[elemento].append(dupla_aux[0])
                elif dupla_aux[0] == elemento:
                    comunicaciones[elemento].append(dupla_aux[1])
    return (comunicaciones)

def crear_listado_cuevas(entrada):
    listado = []
    for dupla in entrada:
        listado.append(dupla[0])
        listado.append(dupla[1])
    set_listado = set(listado)
    return list(set_listado)
    

def es_camino_valido(camino, ya_visitadas, inicio, comodin, veces_usado_comodin):
    camino.append(inicio)
    if (inicio.islower() and inicio != comodin): #No comodin
        ya_visitadas.append(inicio)
    elif (inicio.islower() and inicio == comodin): #Es el comodin
        if (veces_usado_comodin == 0): #Primera vez
            veces_usado_comodin = 1
        else:
            ya_visitadas.append(inicio)
            veces_usado_comodin = 2
    if inicio == "end" and veces_usado_comodin == 2:
        camino_aux = camino.copy()
        caminos_validos.append(camino_aux)
    else:
        opciones = list(set(direcciones[inicio]) - set(ya_visitadas))
        for destino in opciones:
            es_camino_valido(camino, ya_visitadas, destino, comodin, veces_usado_comodin)
            
    camino.pop(-1)
    if (inicio.islower() and inicio != comodin):
        ya_visitadas.pop(-1)
    elif (inicio.islower() and inicio == comodin): #Es el comodin
        if (veces_usado_comodin == 1): #Primera vez
            veces_usado_comodin = 0
        else:
            ya_visitadas.pop(-1)
            veces_usado_comodin = 1 
                

entrada = (interpretar_input(get_input()))
direcciones = (crear_diccionarios(entrada))
lista_cuevas = (crear_listado_cuevas(entrada))

#Creamos lista comodines
lista_comodines = []
for cueva in lista_cuevas:
    if (cueva.islower() and cueva != "start" and cueva != "end"):
        lista_comodines.append(cueva)

#Almacenaremos los caminos aquí
caminos_validos = []

#Caminos sin comodin
print("Sin comodin")
es_camino_valido(camino= [], ya_visitadas=[], inicio= "start", comodin = "", veces_usado_comodin= 2)
for camino in caminos_validos:
        print(camino)


#Caminos con comodin
for comodin in lista_comodines:
    print ("Comodin %s"%comodin)
    es_camino_valido(camino= [], ya_visitadas=[], inicio= "start", comodin = comodin, veces_usado_comodin= 0)
    for camino in caminos_validos:
        print(camino)
print("Total: %s caminos validos"%len(caminos_validos))


