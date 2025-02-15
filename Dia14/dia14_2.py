
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
        duplas.append(cadena[pos_letra]+ cadena[pos_letra+1])
    return duplas

def get_numero_duplas(contador_duplas):
    contador_duplas_copia = contador_duplas.copy()
    tipos_duplas = list(contador_duplas.keys())
    contador_duplas_devolucion = contador_duplas_vacio()
    for tipo_dupla in tipos_duplas:
        duplas_a_anadir = get_duplas_resultantes(tipo_dupla)
        contador_duplas_devolucion[duplas_a_anadir[0]] +=1*contador_duplas_copia[tipo_dupla]
        contador_duplas_devolucion[duplas_a_anadir[1]] +=1*contador_duplas_copia[tipo_dupla]
    return contador_duplas_devolucion

def contador_duplas_vacio ():
    dic_dev = {}
    for key in listado_duplas:
        dic_dev[key] = 0
    return dic_dev
def get_duplas_resultantes (dupla):
    letra1 = (list(str(dupla))) [0]
    letra3 = (list(str(dupla))) [1]
    letra2 = reglas[dupla] 
    return [letra1+letra2, letra2+letra3]

def get_posibles_cadenas_resultantes ():
    keys = list(reglas.keys())
    registro_duplas = []
    for key in keys:
        if (key == "NS"):
            print ("")
        letra1 = (list(str(key))) [0]
        letra3 = (list(str(key))) [1]
        letra2 = reglas[key]
        registro_duplas.append(letra1 + letra3)
        registro_duplas.append(letra1+letra2)
        registro_duplas.append(letra2+letra3)
    return registro_duplas



def contar_duplas(registro_duplas, listado_duplas):
    contador_duplas = {}
    for dupla in listado_duplas:
        contador_duplas[dupla] = 0
    
    for dupla in registro_duplas:
        for tipo_dupla in listado_duplas:
            if (dupla == tipo_dupla):
                contador_duplas[dupla] += 1
            
    return contador_duplas

def crear_contar_letras ():
    listado_letras = set(reglas.values())
    contador = {}
    for letra in listado_letras:
        contador[letra] = 0
    return contador

def contar_letras(contador_duplas, contador):
    keys = list(contador_duplas.keys())
    
    for dupla in keys:
        letra1 = list(dupla)[0]
        letra2 = list(dupla)[1]
        contador[letra1] += contador_duplas[dupla]
        contador[letra2] += contador_duplas[dupla]
        
    for letra in list(contador.keys()):
            contador[letra] = int(contador[letra] /2 ) #Todas las letras están contadas dos veces (estan en dos duplas)
    #Se suma uno al contador correspondiente a la primera y ultima letra pues no estaban en dos duplas        
    contador[cadena[0]] +=1
    contador[cadena[-1]] += 1
    return contador

cadena = get_cadena(get_input())
reglas = get_reglas(get_input())
contador_letras = crear_contar_letras()
listado_duplas = set(get_posibles_cadenas_resultantes())
duplas_dia1 = get_duplas(cadena)
contador_duplas = contar_duplas(duplas_dia1, listado_duplas) #Contador duplas antes de empezar
#Hacer pasar 40 pasos
for _ in range (40):
    contador_duplas = (get_numero_duplas(contador_duplas))
lista_contador_letras = (contar_letras(contador_duplas, contador_letras))
#El resultado es la diferencia entre el elemento mas y menos comun
print(max(list(lista_contador_letras.values()))-min(list(lista_contador_letras.values())))
