import re
''' 
Part One - 
Part Two - 
'''

DIRECTIONS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def add_coords(a, b):
    return (a[0] + b[0], a[1] + b[1])


def walk(grid, path, start_col):
    pos = 0, start_col
    facing = 0  # 0 => right, 1 => down, 2 => left, 3 => up
    direction = DIRECTIONS[facing]
    for (steps, next_direction) in path:
        for _ in range(steps):
            next_pos = add_coords(pos, direction)
            if next_pos in grid:
                if grid[next_pos] is True:
                    pos = next_pos
                elif grid[next_pos] is False:
                    break
            else:
                if facing == 0:
                    wrap_pos = min([
                        tile for tile in grid if tile[0] == pos[0]
                    ])
                elif facing == 1:
                    wrap_pos = min([
                        tile for tile in grid if tile[1] == pos[1]
                    ])
                elif facing == 2:
                    wrap_pos = max([
                        tile for tile in grid if tile[0] == pos[0]
                    ])
                elif facing == 3:
                    wrap_pos = max([
                        tile for tile in grid if tile[1] == pos[1]
                    ])
                if grid[wrap_pos] is False:
                    break
                pos = wrap_pos
        if next_direction == 'R':
            facing += 1
        else:
            facing -= 1
        facing %= 4
        direction = DIRECTIONS[facing]
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing


def part_one(input):
    grid = {}
    start_col = None

    for row_idx, row, in enumerate(input):
        if input[row_idx] == '':
            row_idx += 1
            break
        for col_idx, tile in enumerate(row):
            if tile == '.':
                if start_col is None:
                    start_col = col_idx
                grid[(row_idx, col_idx)] = True
            elif tile == '#':
                grid[(row_idx, col_idx)] = False

    moves = re.findall(r'\d+\D', input[row_idx])
    path = [(int(move[:-1]), move[-1]) for move in moves]
    res = walk(grid, path, start_col)
    return res


def part_two(input):
    board = input[:-2]
    ops = input[-1]

    wrap = {}

    # Front:
    edge(wrap, (0, 50), (1, 0), (0, -1), (149, 0), (-1, 0), (0, -1), 2)  # Left
    edge(wrap, (0, 50), (0, 1), (-1, 0), (150, 0), (1, 0), (0, -1), 1)  # Top

    # Right:
    edge(wrap, (49, 100), (0, 1), (1, 0), (50, 99), (1, 0), (0, 1), 1)  # Under
    edge(wrap, (0, 100), (0, 1), (-1, 0), (199, 0), (0, 1), (1, 0), 0)  # Top
    edge(wrap, (0, 149), (1, 0), (0, 1), (149, 99), (-1, 0), (0, 1), 2)  # Back

    # Under:
    edge(wrap, (50, 50), (1, 0), (0, -1), (100, 0), (0, 1), (-1, 0), 3)  # Left

    # Back:
    edge(wrap, (149, 50), (0, 1), (1, 0), (150, 49), (1, 0), (0, 1), 1)  # Top

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    p, facing = (0, board[0].index('.')), 0
    i = step = 0
    while i < len(ops):
        step += 1
        if ops[i] == 'L':
            facing = (facing-1) % 4
            i += 1
        elif ops[i] == 'R':
            facing = (facing+1) % 4
            i += 1
        else:
            steps = ''
            while i < len(ops) and ops[i].isnumeric():
                steps += ops[i]
                i += 1
            for k in range(int(steps)):
                r1, c1 = p[0] + dir[facing][0], p[1] + dir[facing][1]
                f0 = facing

                if (r1, c1) in wrap:
                    (r1, c1), ff = wrap[(r1, c1)]
                    facing = (facing + ff) % 4

                if board[r1][c1] == '#':
                    facing = f0
                    break
                p = (r1, c1)
    end = (p[0]+1, p[1]+1)
    return end[0]*1000 + end[1]*4 + facing


def edge(wrap, face1, dir1, exit, face2, dir2, enter, rot):
    for k in range(50):
        p1 = (face1[0] + dir1[0] * k, face1[1] + dir1[1] * k)
        p2 = (face2[0] + dir2[0] * k, face2[1] + dir2[1] * k)
        wrap[(p1[0] + exit[0], p1[1] + exit[1])] = (p2, rot)
        wrap[(p2[0] + enter[0], p2[1] + enter[1])] = (p1, -rot)
