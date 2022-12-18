''' 
Part One - What is the surface area of your scanned lava droplet?
Part Two - What is the exterior surface area of your scanned lava droplet?
'''


def neighbors(cube):
    deltas = [
        (1,  0,  0),
        (-1,  0,  0),
        (0,  1,  0),
        (0, -1,  0),
        (0,  0,  1),
        (0,  0, -1),

    ]
    x, y, z = cube
    for dx, dy, dz in deltas:
        yield (x+dx, y+dy, z+dz)


def enclosed_cubes(cubes):
    enclosed = set()
    not_enclosed = set()

    xmin = min(cube[0] for cube in cubes)
    xmax = max(cube[0] for cube in cubes)

    ymin = min(cube[1] for cube in cubes)
    ymax = max(cube[1] for cube in cubes)

    zmin = min(cube[2] for cube in cubes)
    zmax = max(cube[2] for cube in cubes)

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                cube = (x, y, z)
                if cube in cubes:
                    continue

                has_neighbors = [
                    any((n_x, y, z) in cubes for n_x in range(xmin, x)),
                    any((n_x, y, z) in cubes for n_x in range(x + 1, xmax + 1)),
                    any((x, n_y, z) in cubes for n_y in range(ymin, y)),
                    any((x, n_y, z) in cubes for n_y in range(y + 1, ymax + 1)),
                    any((x, y, n_z) in cubes for n_z in range(zmin, z)),
                    any((x, y, n_z) in cubes for n_z in range(z + 1, zmax + 1)),
                ]
                if all(has_neighbors):
                    enclosed.add(cube)
                else:
                    not_enclosed.add(cube)

    size = 0
    while size != len(enclosed):
        size = len(enclosed)
        for ecube in list(enclosed):
            for n in neighbors(ecube):
                if n in not_enclosed:
                    not_enclosed.add(ecube)
                    if ecube in enclosed:
                        enclosed.remove(ecube)

    return enclosed


def parse_cubes(input):
    cubes = set()
    for coord in input:
        x, y, z = map(int, coord.split(','))
        cubes.add((x, y, z))
    return cubes


def part_one(input):
    cubes = parse_cubes(input)

    area = sum((
        1 for cube in cubes for neighbor in neighbors(cube)
        if neighbor not in cubes
    ))
    return area


def part_two(input):
    cubes = parse_cubes(input)
    encloused = enclosed_cubes(cubes)
    area = sum((
        1 for cube in cubes for neighbor in neighbors(cube)
        if neighbor not in cubes and neighbor not in encloused
    ))
    return area
