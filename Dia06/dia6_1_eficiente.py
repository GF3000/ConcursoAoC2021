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

def agrupar_peces_por_estado(lista):
    listaaux = [0] * 9
    for element in lista:
        listaaux[element] += 1
    return listaaux
    #Esta nueva lista cuenta cuantos peces hay en cada día, los que estab en dia 0 estan en pos 0, los de 1 en 1...



def pasar_dia(lista):
    listaux = [0] * 9
    listaux[0] = lista[1]
    listaux[1] = lista[2]
    listaux[2] = lista[3]
    listaux[3] = lista[4]
    listaux[4] = lista[5]
    listaux[5] = lista[6]
    listaux[6] = lista[0] + lista[7] #Coge los peces niños mas los peces que acaban de tener un hijo
    listaux[7] = lista[8]
    listaux[8] = lista[0]
    return listaux

def pasar_n_dias (dias):
    lista_eficiente = agrupar_peces_por_estado(listasalida)
    for _ in range(dias):
        lista_eficiente = pasar_dia(lista_eficiente)
    return (lista_eficiente)

listasalida = get_input()
listasalida = interpretar_input(listasalida) 
print(sum(pasar_n_dias(80)))
