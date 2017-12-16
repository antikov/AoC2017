def get_coord(coord):
    arr = {"n":(0,1),"ne":(1,0.5),"nw":(-1,0.5),"sw":(-1,-0.5),"s":(0,-1),"se":(1,-0.5)}
    return arr[coord]

def get_distance(coord):
    return abs(coord[0]) + coord[0]/2 - coord[1]

f = list(map(get_coord,open("input").read().strip().split(",")))
i, j = 0, 0
max_distance = 0
for coord in f:
    i += coord[0]
    j += coord[1]
    max_distance = max(max_distance,get_distance((i,j)))

print("Part 1:",get_distance((i,j)))
print("Part 2:",max_distance)
