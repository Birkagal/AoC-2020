'''
Part One - Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?
Part Two - simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?
'''


def count_active_neighbors_3d(cube, x, y, z):
    active_neighbors = 0
    for neighbor_x in range(x-1, x+2):
        for neighbor_y in range(y-1, y+2):
            for neighbor_z in range(z-1, z+2):
                if (neighbor_x, neighbor_y, neighbor_z) in cube:
                    active_neighbors += 1
    if (x, y, z) in cube:
        active_neighbors -= 1
    return active_neighbors


def get_grid_bounds_3d(cube):
    lox = min(map(lambda p: p[0], cube))
    loy = min(map(lambda p: p[1], cube))
    loz = min(map(lambda p: p[2], cube))
    hix = max(map(lambda p: p[0], cube))
    hiy = max(map(lambda p: p[1], cube))
    hiz = max(map(lambda p: p[2], cube))
    return range(lox-1, hix+2), range(loy-1, hiy+2), range(loz-1, hiz+2)


def cycle_cube_3d(cube):
    next_cycle = set()
    rangex, rangey, rangez = get_grid_bounds_3d(cube)
    for x in rangex:
        for y in rangey:
            for z in rangez:
                active_neighbors = count_active_neighbors_3d(cube, x, y, z)
                if ((x, y, z) in cube and active_neighbors in [2, 3]) or active_neighbors == 3:
                    next_cycle.add((x, y, z))
    return next_cycle


def partOne(content):
    cube = set()
    for x, row in enumerate(content):
        for y, cell in enumerate(row):
            if cell == '#':
                cube.add((x, y, 0))
    for _ in range(6):
        cube = cycle_cube_3d(cube)
    return len(cube)


def count_active_neighbors_4d(cube, x, y, z, w):
    active_neighbors = 0
    for neighbor_x in range(x-1, x+2):
        for neighbor_y in range(y-1, y+2):
            for neighbor_z in range(z-1, z+2):
                for neighbor_w in range(w-1, w+2):
                    if (neighbor_x, neighbor_y, neighbor_z, neighbor_w) in cube:
                        active_neighbors += 1
    if (x, y, z, w) in cube:
        active_neighbors -= 1
    return active_neighbors


def get_grid_bounds_4d(cube):
    lox = min(map(lambda p: p[0], cube))
    loy = min(map(lambda p: p[1], cube))
    loz = min(map(lambda p: p[2], cube))
    low = min(map(lambda p: p[3], cube))
    hix = max(map(lambda p: p[0], cube))
    hiy = max(map(lambda p: p[1], cube))
    hiz = max(map(lambda p: p[2], cube))
    hiw = max(map(lambda p: p[3], cube))
    return range(lox-1, hix+2), range(loy-1, hiy+2), range(loz-1, hiz+2), range(low-1, hiw+2)


def cycle_cube_4d(cube):
    next_cycle = set()
    rangex, rangey, rangez, rangew = get_grid_bounds_4d(cube)
    for x in rangex:
        for y in rangey:
            for z in rangez:
                for w in rangew:
                    active_neighbors = count_active_neighbors_4d(
                        cube, x, y, z, w)
                    if ((x, y, z, w) in cube and active_neighbors in [2, 3]) or active_neighbors == 3:
                        next_cycle.add((x, y, z, w))

    return next_cycle


def partTwo(content):
    cube = set()
    for x, row in enumerate(content):
        for y, cell in enumerate(row):
            if cell == '#':
                cube.add((x, y, 0, 0))
    for _ in range(6):
        cube = cycle_cube_4d(cube)
    return len(cube)
