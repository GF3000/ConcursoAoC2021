def get_input():
    listsalida = []
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        entrada[entrada.index(i)] = i.replace("\n", "")
    
    return entrada

def interpretar_input(input):
    lista_dev = []
    for fila in input:
        
        lista_dev.append(fila.split(" "))
    
    for fila in lista_dev:
        lista_dev[lista_dev.index(fila)] = fila[-4:]
    return lista_dev

def contar_segmentos_unicos(fila):
    contar_unicos = 0
    for element in fila:
        if len(element) == 2 or len(element) == 4 or len(element) == 3 or len(element) == 7:
            contar_unicos += 1
    return contar_unicos
    
def contar_seg_uni_en_lista (lista):
    contar_total = 0
    for fila in lista:
        contar_total += contar_segmentos_unicos(fila)
    return contar_total

listado_segmentos = (interpretar_input(get_input()))

print(contar_seg_uni_en_lista(listado_segmentos))