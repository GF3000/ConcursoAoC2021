def get_input():
    
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        entrada[entrada.index(i)] = i.replace("\n", "")
    
    return entrada

def interpretar_input(input):
    input_interpretada = []
    for fila in input:
        input_interpretada.append([])
        for numero in fila:
            input_interpretada[input.index(fila)].append(int(numero))
    return input_interpretada

def get_cadena(input):
    cadena = []
    str_cadena = input[0]
    cadena = list(str_cadena)
    return cadena

def get_reglas(input):
    copia = input.copy()
    copia.pop(0)
    copia.pop(0)
    
    lista_duplas = []
    for fila in copia:
        str_dividido = fila.split()
        lista_duplas.append([str_dividido[0], str_dividido[2]])

    diccionario = {}
    for dupla in lista_duplas:
        diccionario[dupla[0]] = dupla [1]
    return diccionario

def get_duplas(cadena):
    duplas = []
    for pos_letra in range (len(cadena)-1):
        duplas.append([cadena[pos_letra], cadena[pos_letra+1]])
    return duplas

def incorporar_elemento (dupla):
    elemento = str (dupla[0] + dupla[1])
    elemento_anadido = reglas [elemento]
    devolucion = str(elemento_anadido + dupla[1])
    return devolucion

def ampliar_cadena (cadena):
    lista_duplas = get_duplas(cadena)

    cadena_devolucion = cadena[0]
    for dupla in lista_duplas:
        cadena_devolucion += incorporar_elemento(dupla)
    return cadena_devolucion

def pasan_n_dias (cadena, dias):
    
    for _ in range (dias):
        cadena = ampliar_cadena(cadena)
    return cadena

def contar_elementos (cadena, listado_letras):
    #Creamos un diccionario para contar las veces que se repite cada letra
    contador_letras = {}
    for letra in listado_letras:
        contador_letras[letra] = 0
    
    for elemento in cadena:
        for letra in listado_letras:
            if (elemento == letra):
                contador_letras[letra] += 1
    
    return contador_letras

cadena = get_cadena(get_input())
reglas = get_reglas(get_input())
listado_letras = set(reglas.values())
cadena = pasan_n_dias(cadena, 10)
lista_contador_letras = contar_elementos(cadena, listado_letras)

#El resultado es la diferencia entre el elemento mas y menos comun
print(max(list(lista_contador_letras.values())) - min(list(lista_contador_letras.values())))