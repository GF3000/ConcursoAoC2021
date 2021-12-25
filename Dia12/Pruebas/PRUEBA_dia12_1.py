   
caminos_validos = []
def es_camino_valido(camino, ya_visitadas, inicio):
    camino.append(inicio)
    if (inicio.islower()):
        ya_visitadas.append(inicio)
    if inicio == "end":
        camino_aux = camino.copy()
        caminos_validos.append(camino_aux)
    else:
        opciones = list(set(direcciones[inicio]) - set(ya_visitadas))
        for destino in opciones:
            es_camino_valido(camino, ya_visitadas, destino)
            
    camino.pop(-1)
    if (inicio.islower()):
        ya_visitadas.pop(-1)
    
            
                

direcciones = {"start": ["A", "b","c"], "A": ["start", "b"], "b":["A", "start", "c", "d"], "c":["start", "b", "E"], "E": ["c", "d"], "d":["b", "E", "end"], "end":["d"]}
lista_cuevas = ["start", "A", "b", "c", "E", "d", "end"]

(es_camino_valido(camino= [], ya_visitadas=[], inicio= "start"))
for camino in caminos_validos:
    print(camino)
print("Total: %s caminos validos"%len(caminos_validos))

