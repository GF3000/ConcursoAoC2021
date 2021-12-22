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

def contar_elemento(cadena, simbolos):
    cadena = list(cadena)
    lstkey = list(simbolos.keys())
    cadena_abiertos = []
    for i in cadena:
        if i in lstkey:
            cadena_abiertos.append(i)
        else:
            if i == ")":
                if cadena_abiertos[-1] != "(":
                    return 3
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == "}":
                if cadena_abiertos[-1] != "{":
                    return 1197
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == ">":
                if cadena_abiertos[-1] != "<":
                    return 25137
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == "]":
                if cadena_abiertos[-1] != "[":
                    return 57
                else:
                    cadena_abiertos.pop(-1)
    return 0
                    

            
        



        
entrada = get_input()

simbolos = {"[":"]", "(":")", "<":">", "{":"}"}
suma_puntos = 0

for cadena in entrada:
    suma_puntos += contar_elemento(cadena, simbolos)

print (suma_puntos)
