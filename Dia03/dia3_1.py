#lectura del input
with open("input.txt") as f:
    entrada = f.readlines()
listsalida = []
for i in entrada:
   listsalida.append (i.replace("\n", ""))
#funciones
def strListToList(str):
    listaaux =[]
    for i in listsalida:
        listaaux.append([])
        for j in i:
            listaaux[listsalida.index(i)].append(j)
    return listaaux
def binToInt(bin):
    lstbin =[]
    for i in bin:
        lstbin.append(i)
    print(lstbin)
    nInt = 0
    for i in range (0, len(lstbin)):
        nInt += int(lstbin[i]) * pow(2,len(lstbin)-1-i) 
    return nInt

#codigo
listaaux = strListToList(listsalida)
binganma = ""
binepsilon = ""


for j in range(0, len(listaaux[1])):#Para crear el binario de ganma
    contar0 = 0
    contar1 = 0
    #print(j)
    for i in listaaux:
        
        for n in i[j]:
            #print(i[j])
            if n == "0":
                #print("+0")
                contar0 += 1
            elif n == "1":
                #print("+1")
                contar1 += 1
    
    if contar0 < contar1:
        binganma += "1"
    elif contar1 < contar0:
        binganma += "0"
    
for j in range(0, len(listaaux[1])):#Para crear el binario de epsilon
    contar0 = 0
    contar1 = 0
    #print(j)
    for i in listaaux:
        
        for n in i[j]:
            #print(i[j])
            if n == "0":
                #print("+0")
                contar0 += 1
            elif n == "1":
                #print("+1")
                contar1 += 1
    
    if contar0 < contar1:
        binepsilon += "0"
    elif contar1 < contar0:
        binepsilon += "1"

print(binToInt(binepsilon)* binToInt(binganma))

