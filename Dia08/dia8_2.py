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
    
    
    return lista_dev

def get_codigo(fila):
    dic_elementos = {1: buscar_elemento_1(fila), 4 : buscar_elemento_4(fila), 7: buscar_elemento_7(fila), 8 : buscar_elemento_8(fila)}
    dic_elementos[3] = buscar_elemento_3(fila, dic_elementos[1])
    dic_elementos[6] = buscar_elemento_6(fila, dic_elementos[1])
    dic_elementos[9] = buscar_elemento_9(fila,dic_elementos[4])
    dic_elementos[0] = buscar_elemento_0(fila, dic_elementos[6], dic_elementos[9])
    dic_elementos[2] = buscar_elemento_2(fila,dic_elementos[8],dic_elementos[9])
    dic_elementos[5] = buscar_elemento_5(fila,dic_elementos[8], dic_elementos[2])
    return dic_elementos

def aplicar_codigo(fila, codigo):
    digitos_out = fila[-4:]
    lista_segmentos =  list((codigo.keys()))
    
    display = []
    for element in digitos_out:
        digitos_out[digitos_out.index(element)] = set (element)
    for digito in digitos_out:
        for numero in lista_segmentos:
            if set(digito) == set(codigo[numero]):
                display.append(numero)
    str_display = ""
    for numero in display:
        str_display += str(numero)
    return(int(str_display))  
    
def contenida (lista_pequena, lista_grande):
    contenida = True
    for element in lista_pequena:
        if element not in lista_grande:
            contenida = False
    return contenida

def buscar_elemento_1(fila):
    for element in fila:
        if len(element) == 2:
            return list(element)

def buscar_elemento_4(fila):
    for element in fila:
        if len(element) == 4:
            return list(element)

def buscar_elemento_7(fila):
    for element in fila:
        if len(element) == 3:
            return list(element)

def buscar_elemento_8(fila):
    for element in fila:
        if len(element) == 7:
            return list(element)

def buscar_elemento_6(fila, elemento1):
    for element in fila:
        if len(element) == 6:
            if(elemento1[0] in element and elemento1[1] not in element):
                return list(element)
            elif(elemento1[1] in element and elemento1[0] not in element):
                return list(element)
                
def buscar_elemento_3(fila, elemento1):
    for element in fila:
        if len(element) == 5:
            if(elemento1[0] in element and elemento1[1] in element):
                return list(element) 

def buscar_elemento_9(fila, elemento4):
    for element in fila:
        if len(element) == 6:
            if (contenida(elemento4,element)):
                return list(element)

def buscar_elemento_0(fila, elemento6, elemento9):
    for element in fila:
        if len(element) == 6:
            if list(element) != elemento6 and list(element)!= elemento9:
                return list(element)         

def buscar_elemento_2(fila, elemento8, elemento9):
    for element in fila:
        if len(element) == 5:
            if contenida((set(elemento8)-set(elemento9)),element):
                return list(element)

def buscar_elemento_5(fila, elemento8, elemento2):
    for element in fila:
        if len(element) == 5:
            if contenida((set(elemento8)-set(elemento2)),element):
                return list(element)

def crear_lista_display(listado):
    listado_display = []
    for fila in listado:
        codigo = get_codigo(fila)
        listado_display.append(aplicar_codigo(fila, codigo))
    return listado_display

listado_segmentos = (interpretar_input(get_input()))
print(sum(crear_lista_display(listado_segmentos)))