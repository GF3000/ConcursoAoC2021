def get_input():
    
    with open("input.txt") as f:
        entrada = f.readlines()
    
    for i in entrada:
        entrada[entrada.index(i)] = i.replace("\n", "")
    
    return entrada


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
                    return 0
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == "}":
                if cadena_abiertos[-1] != "{":
                    return 0
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == ">":
                if cadena_abiertos[-1] != "<":
                    return 0
                else:
                    cadena_abiertos.pop(-1)
                    
            elif i == "]":
                if cadena_abiertos[-1] != "[":
                    return 0
                else:
                    cadena_abiertos.pop(-1)
    #Si no ha saltado ningún error es que está incompleta
    return cual_falta(cadena_abiertos)
                    

            
def cual_falta (cadena_abierta):
    cadena_faltan = []
    cadena_abierta.reverse()
    for simbolo_abierto in cadena_abierta:
        cadena_faltan.append(simbolos.get(simbolo_abierto))

    score = 0
    for simbolo_faltante in cadena_faltan:
        score *= 5
        if simbolo_faltante == ")":
            score+=1
        elif simbolo_faltante == "]":
            score+=2
        elif simbolo_faltante == "}":
            score+=3
        elif simbolo_faltante == ">":
            score+=4
    return score



        
entrada = get_input()

simbolos = {"[":"]", "(":")", "<":">", "{":"}"}
cadena_puntos = []
for cadena in entrada:
    cadena_puntos.append(contar_elemento(cadena, simbolos))
while 0 in cadena_puntos:
    cadena_puntos.remove(0)
cadena_puntos.sort()
punto_medio = int(len(cadena_puntos)/2)
print (cadena_puntos[punto_medio])
