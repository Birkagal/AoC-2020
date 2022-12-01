'''
Part One - After all of the instructions have been followed, how many tiles are left with the black side up?
Part Two - How many tiles will be black after 100 days?
'''

DELTA_MOVES = {
    'e': (1,  0),
    'w': (-1,  0),
    'se': (1,  1),
    'sw': (0,  1),
    'ne': (0, -1),
    'nw': (-1, -1)
}


def parse_data(data):
    all_moves = []
    line_moves = []
    current_move = ''
    for line in data:
        for char in line:
            current_move += char
            if char == 'e' or char == 'w':
                line_moves.append(current_move)
                current_move = ''
        all_moves.append(line_moves)
        line_moves = []
    return all_moves


def move(moves):
    x, y = 0, 0
    for move in moves:
        delta_x, delta_y = DELTA_MOVES[move]
        x += delta_x
        y += delta_y
    return x, y


def count_black_neighbors(grid, x, y):
    deltas = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
    neighbors = 0
    for delta_x, delta_y in deltas:
        if (x+delta_x, y+delta_y) in grid:
            neighbors += 1
    return neighbors


def get_all_neighbors(grid):
    deltas = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
    points = set()
    for x, y in grid:
        for delta_x, delta_y in deltas:
            points.add((x+delta_x, y+delta_y))
    return points


def play_turn(grid):
    new_state = set()

    for point in get_all_neighbors(grid):
        point_neighbors = count_black_neighbors(grid, point[0], point[1])
        if point in grid and not (point_neighbors == 0 or point_neighbors > 2):
            new_state.add(point)
        elif point not in grid and point_neighbors == 2:
            new_state.add(point)
    return new_state


def part_one(content):
    all_moves = parse_data(content)
    black_hex_in_grid = set()

    for moves in all_moves:
        point = move(moves)
        if point in black_hex_in_grid:
            black_hex_in_grid.remove(point)
        else:
            black_hex_in_grid.add(point)
    return len(black_hex_in_grid)


def part_two(content):
    all_moves = parse_data(content)
    grid = set()
    for moves in all_moves:
        point = move(moves)
        if point in grid:
            grid.remove(point)
        else:
            grid.add(point)

    for _ in range(100):
        grid = play_turn(grid)
    return len(grid)
