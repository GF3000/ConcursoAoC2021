
with open("input.txt") as file:
    data = [[int(pos) for pos in list(line.strip())] for line in file.readlines()]
    data = [[0]*len(data[0])] + data + [[0]*len(data[0])]
    data = [[0] + line + [0] for line in data]

stack = []
part1 = 0
part2 = 0
while True:
    part2 += 1
    flashed = []
    for r in range(1, len(data)-1):
        for c in range(1, len(data[0])-1):
            if data[r][c] == 9:
                stack.append((r,c))
                while stack:
                    x,y = stack.pop()
                    if data[x][y] == 9:
                        data[x][y] = 0
                        flashed.append((x,y))
                        part1 += 1
                        for px, py in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1, -1), (-1,1), (1, -1)]:
                            if all([x+px != 0, y+py != 0, y+py != len(data)-1, x+px != len(data)-1]):
                                stack.append((x+px, y+py))
                    elif (x,y) not in flashed:
                        data[x][y] += 1
            elif (r,c) not in flashed:
                data[r][c] += 1
    if len(flashed) == (len(data)-2) * (len(data)-2):
        break

print(part1)
print(part2)