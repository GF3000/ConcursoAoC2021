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



def caminos(ya_visitadas, diccionario, inicio):
    if (inicio.islower()):
       ya_visitadas.append(inicio)
       set_visitadas_aux = set(ya_visitadas)
       ya_visitadas = list (set_visitadas_aux)
    opciones = list(set(diccionario[inicio]) - set(ya_visitadas))
    if (len(opciones) == 0):
        return 0
    for destino in opciones:
        print(destino)
        if (destino.isupper()):
            return (1 + caminos(ya_visitadas, diccionario, destino))
        else:
            set_aux = set(ya_visitadas)
            set_aux.add(destino)
            new_ya_visitadas = list(set_aux)
            return (1 + caminos(new_ya_visitadas, diccionario, destino))
    

caminos_validos = []

def es_camino_valido(camino, ya_visitadas, inicio, comodin):
    camino.append(inicio)
    b_usado_comodin = False
    if (inicio.islower() and inicio != comodin):
        ya_visitadas.append(inicio)
    elif (inicio.islower() and inicio == comodin):
        b_usado_comodin = True
        comodin = ""
    if inicio == "end":
        camino_aux = camino.copy()
        caminos_validos.append(camino_aux)
    else:
        opciones = list(set(direcciones[inicio]) - set(ya_visitadas))
        for destino in opciones:
            es_camino_valido(camino, ya_visitadas, destino, comodin)
            
    camino.pop(-1)
    if (inicio.islower() and not b_usado_comodin):
        ya_visitadas.pop(-1)
    elif (inicio.islower() and b_usado_comodin):
        comodin = inicio
    
            
                
           
    

entrada = (interpretar_input(get_input()))
direcciones = (crear_diccionarios(entrada))
lista_cuevas = (crear_listado_cuevas(entrada))
lista_cuevas_minusculas = []
for cuevas in lista_cuevas:
    if cuevas.islower() and cuevas != "end" and cuevas != "start":
        lista_cuevas_minusculas.append(cuevas)

suma_caminos_validos= 0
lisya_caminos_validos = []
lista_aux = []
for comodin in lista_cuevas_minusculas:
    es_camino_valido(camino= [], ya_visitadas=[], inicio= "start",comodin = comodin)
    suma_caminos_validos += len(caminos_validos)
    lisya_caminos_validos.append(caminos_validos)
    # print ("Con el comodin %s hay %s"%(comodin, len(caminos_validos)))
    # for camino in caminos_validos:
    #    print(camino)
    caminos_validos = []

for comodin in lisya_caminos_validos:
    for camino in comodin:
        print(camino)
        if (camino not in lista_aux):
            lista_aux.append(camino)

print(len(lista_aux))
#(es_camino_valido(camino= [], ya_visitadas=[], inicio= "start"))
# for camino in caminos_validos:
#     print(camino)
# print("Total: %s caminos validos"%len(caminos_validos))
print(suma_caminos_validos)