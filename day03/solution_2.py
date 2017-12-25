NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction

def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = NORTH # initial direction
    matrix = [[0] * width for _ in range(height)]
    matrix[y][x] = 1
    count = 0
    number = 0
    while number < 265149:
        count += 1
        matrix[y][x] = matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] + \
        matrix[y][x-1] + matrix[y][x] + matrix[y][x+1] + \
        matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1]
        number = matrix[y][x]
        #matrix[y][x] = count
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is 0): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go
    return number

print(spiral(100, 100))
