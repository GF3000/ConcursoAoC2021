def get_input():
    listsalida = []
    with open("input.txt") as f:
        entrada = f.readlines()
    
    entrada = entrada[0].split(",")
    
    for i in entrada:
        listsalida.append (i.replace("\n", ""))
    return listsalida

def interpretar_input(lista):
    lista_copia = lista.copy()
    for i in lista_copia:
        lista_copia[lista_copia.index(i)] = int(i)
    return lista_copia

def pasa_un_dia(lista):
    for i in range(len(lista)):
        lista[i] -= 1
    reproducirse(lista)

def reproducirse(lista):
    for i in range(len(lista)):
        if lista[i] == -1:
            lista[i] = 6
            lista.append(8)
def pasan_n_dias (dias, lista):
    for i in range (dias):
        pasa_un_dia(lista)

listasalida = get_input()
listasalida = interpretar_input(listasalida)
pasan_n_dias(80, listasalida)
print(len(listasalida))


