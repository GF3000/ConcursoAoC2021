with open("input.txt") as f:
    entrada = f.readlines()
listasalida = []
for i in entrada:
   listasalida.append (i.replace("\n", ""))


deep = 0
horpos = 0
aim = 0

for i in listasalida:
    ordenes = i.split()
    if ordenes[0] == "up":
        aim -= int(ordenes[1])
    elif ordenes[0] == "down":
        aim += int(ordenes[1])
    elif ordenes[0] == "forward":
        horpos += int(ordenes[1])
        deep += aim* int(ordenes[1])


print(deep*horpos)