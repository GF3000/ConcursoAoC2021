with open("input.txt") as f:
    entrada = f.readlines()
listasalida = []
for i in entrada:
   listasalida.append (i.replace("\n", ""))


deep = 0
horpos = 0


for i in listasalida:
    ordenes = i.split()
    if ordenes[0] == "up":
        deep -= int(ordenes[1])
    elif ordenes[0] == "down":
        deep += int(ordenes[1])
    elif ordenes[0] == "forward":
        horpos += int(ordenes[1])
        


print(deep*horpos)