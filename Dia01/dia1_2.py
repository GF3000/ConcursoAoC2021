
with open("input.txt") as f:
    entrada = f.readlines()
listsalida = []
for i in entrada:
   listsalida.append (i.replace("\n", ""))

aumentado= 0
listsalida2 = []
for i in range(0,len(listsalida)-2):
    listsalida2.append(int(listsalida[i])+int(listsalida[i+1])+ int(listsalida[i+2]))
#print(listsalida2)
for i in range (1, len(listsalida2)):
    if listsalida2[i] > listsalida2[i-1]:
        aumentado+=1

print(aumentado)
