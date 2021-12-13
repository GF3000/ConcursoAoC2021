import math

f = open('input.txt')
data = [line for line in f.readlines()]

inputs = [line.strip('\n') for line in data]

matrix = []

for idx, line in enumerate(inputs):
    matrix += [[int(x) for x in line]]
counter = 0

low_points = []

row_move = [1,0,-1,0]
column_move = [0,-1,0,1]
listado_low_points = []
# First star
for idx, _ in enumerate(matrix):
    for jdx, _ in enumerate(matrix[0]):
        is_low = True
        for i in range(4):
            r = idx + row_move[i]
            c = jdx + column_move[i]
            if 0<=r<len(matrix) and 0<=c<len(matrix[0]) and matrix[idx][jdx] >= matrix[r][c]:
                is_low = False
                break
        if is_low:
            listado_low_points.append(matrix[idx][jdx])
            counter += matrix[idx][jdx] +1
            low_points += [(idx,jdx)]
            if (matrix[idx][jdx] == 6):
                print(idx)
                print(jdx)

print(listado_low_points)
print(counter)

# Second star
def calc_basin_size(idx, jdx, visited_points):
    if (idx,jdx) in visited_points or matrix[idx][jdx] == 9:
        return
    else:
        visited_points.add((idx,jdx))
        for i in range(4):
            r = idx + row_move[i]
            c = jdx + column_move[i]
            if 0<=r<len(matrix) and 0<=c<len(matrix[0]):
                calc_basin_size(r,c, visited_points)
        return visited_points

basin_size = [0] * 3
for low_point in low_points:
    idx, jdx = low_point
    points = calc_basin_size(idx,jdx, set())
    if basin_size[0] < len(points):
        basin_size[0] = len(points)
        basin_size.sort()
#print(math.prod(basin_size))