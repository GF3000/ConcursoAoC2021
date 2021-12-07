
with open("input.txt") as f:
    entrada = f.readlines()
listsalida = []
for i in entrada:
   listsalida.append (i.replace("\n", ""))

aumentado= 0

for i in range (1, len(listsalida)):
    if listsalida[i] > listsalida[i-1]:
        aumentado+=1

print(aumentado)
