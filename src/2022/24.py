from collections import defaultdict
'''
Part One -
Part Two -
'''


def move_blizzards(blizzards, height, width):
    new = defaultdict(list)
    for (r, c), dirs in blizzards.items():
        for dr, dc in dirs:
            newr = (r + dr) % height
            newc = (c + dc) % width
            new[newr, newc].append((dr, dc))
    return new


def neighbors(bliz, pos, height, width):
    r, c = pos
    neighbors = set()
    # Right above the destination? Even if out of bounds, that's also a valid position to move to.
    if r == 0 and c == 0:
        neighbors.add((-1, 0))
    elif r == height - 1 and c == width - 1:
        neighbors.add((height, c))

    # For each of the 4 cardinal directions...
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        rr, cc = r + dr, c + dc
        # ... check if we are in bounds and if there is NO blizzard here...
        if 0 <= rr < height and 0 <= cc < width and (rr, cc) not in bliz:
            # ... if so, we can move here.
            neighbors.add((rr, cc))

    # We can also stand still if no blizzard hits us.
    if (r, c) not in bliz:
        neighbors.add((r, c))

    return neighbors


def bfs(bliz, src, dst, height, width):
    positions = {src}
    time = 0

    # While the destination is not reached.
    while dst not in positions:
        # Advance time and evolve blizzards moving them around.
        time += 1
        bliz = move_blizzards(bliz, height, width)

        # For each possible position we are tracking, calculate the next valid
        # positions, and add them to a new set.
        new_positions = set()
        for pos in positions:
            neighs = neighbors(bliz, pos, height, width)
            new_positions.update(neighs)

        # Track these new positions in the next iteration.
        positions = new_positions

    return time, bliz


def parse_grid(input):
    DIRMAP = {
        '>': (0,  1),
        '<': (0, -1),
        'v': (1,  0),
        '^': (-1,  0),
    }

    blizzards = defaultdict(list)
    for r, row in enumerate(input[1:-1]):
        for c, cell in enumerate(row[1:-1]):
            if cell in DIRMAP:
                blizzards[r, c].append(DIRMAP[cell])

    return blizzards


def part_one(input):
    height, width = len(input) - 2, len(input[0]) - 2
    src, dst = (-1, 0), (height, width - 1)
    blizzards = parse_grid(input)

    time, _ = bfs(blizzards, src, dst, height, width)
    return time


def part_two(input):
    height, width = len(input) - 2, len(input[0]) - 2
    src, dst = (-1, 0), (height, width - 1)

    blizzards = parse_grid(input)
    time1, blizzards = bfs(blizzards, src, dst, height, width)
    time2, blizzards = bfs(blizzards, dst, src, height, width)
    time3, blizzards = bfs(blizzards, src, dst, height, width)
    return time1+time2+time3
