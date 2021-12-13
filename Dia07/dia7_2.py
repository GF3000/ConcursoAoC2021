def get_input():
    listsalida = []
    with open("input.txt") as f:
        entrada = f.readlines()
    
    entrada = entrada[0].split(",")
    
    for i in entrada:
        listsalida.append (i.replace("\n", ""))
    return listsalida

def interpretar_input (input):
    listadev = []
    for element in input:
        listadev.append(int(element))
    return listadev

def mover_a_posicion_x (x, lista):
    lista_aux = lista.copy()
    fuel  = 0
    for element in lista_aux:
        fuel += sumatorio_hasta_0(abs(x - element))
    return fuel

def probar_todos_los_numeros (lista):
    maximo = max(lista)
    minimo = min(lista)
    fuel_list = []
    for i in range (minimo,maximo):
        fuel_list.append(mover_a_posicion_x(i,lista))
    return fuel_list

def sumatorio_hasta_0 (diferencia):    
    return int((diferencia*(diferencia+1))/2)
    


posicion_crabs = (interpretar_input(get_input()))
print(min(probar_todos_los_numeros(posicion_crabs)))
