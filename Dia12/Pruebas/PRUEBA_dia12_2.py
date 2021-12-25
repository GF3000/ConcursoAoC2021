   
caminos_validos = []
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
            
direcciones = {"start": ["A", "b","c"], "A": ["start", "b"], "b":["A", "start", "c", "d"], "c":["start", "b", "E"], "E": ["c", "d"], "d":["b", "E", "end"], "end":["d"]}
lista_cuevas = ["start", "A", "b", "c", "E", "d", "end"]

#Creamos lista comodines
lista_comodines = []
for cueva in lista_cuevas:
    if (cueva.islower() and cueva != "start" and cueva != "end"):
        lista_comodines.append(cueva)

#Creamos una lista donde irán todos los camninos válidos
listado_total_caminos = []

#Caminos sin comodin
print("Sin comodin")
es_camino_valido(camino= [], ya_visitadas=[], inicio= "start", comodin = "", veces_usado_comodin= 2)
for camino in caminos_validos:
        print(camino)
        listado_total_caminos.append(camino)
caminos_validos = []

#Caminos con comodin
for comodin in lista_comodines:
    print ("Comodin %s"%comodin)
    es_camino_valido(camino= [], ya_visitadas=[], inicio= "start", comodin = comodin, veces_usado_comodin= 0)
    for camino in caminos_validos:
        print(camino)
        listado_total_caminos.append(camino)
    caminos_validos = []
print("Total: %s caminos validos"%len(listado_total_caminos))


