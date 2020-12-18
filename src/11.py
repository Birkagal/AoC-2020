from copy import deepcopy
'''
Part One - Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
Part Two - Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
'''


def first_play_turn(current_state):
    next_state = deepcopy(current_state)
    for i, row in enumerate(current_state):
        for j, cell in enumerate(row):
            if cell == '.':
                continue
            neighbors = first_count_neighbors(current_state, i, j)
            # Evolve a single cell based on rules
            if cell == 'L' and neighbors == 0:
                next_state[i][j] = '#'
            elif cell == '#' and neighbors >= 4:
                next_state[i][j] = 'L'
    return next_state


def first_count_neighbors(grid, row, col):
    diffs = ((-1, 0), (1,  0), (0, 1), (0, -1),  # North, South, East, West
             (-1, 1), (-1, -1), (1, 1), (1, -1))  # NE, NW, SE, SW
    total = 0
    for diff_row, diff_Col in diffs:
        check_row, check_col = row + diff_row, col + diff_Col
        if 0 <= check_row <= (len(grid) - 1) and 0 <= check_col <= (len(grid[0]) - 1):
            # True = 1, False = 0
            total += grid[check_row][check_col] == '#'
    return total


def partOne(content):
    state = [list(line) for line in content]
    grid = deepcopy(state)

    next_state = first_play_turn(grid)
    while state != next_state:
        state = deepcopy(next_state)
        next_state = first_play_turn(next_state)
    return sum(row.count('#') for row in state)


def partTwo(content):
    state = [list(line) for line in content]
    next_state = second_play_turn(state)
    while state != next_state:
        state = deepcopy(next_state)
        next_state = second_play_turn(next_state)
    return sum(row.count('#') for row in state)


def second_play_turn(current_state):
    next_state = deepcopy(current_state)
    for i, row in enumerate(current_state):
        for j, cell in enumerate(row):
            if cell == '.':
                continue
            neighbors = second_count_neighbors(current_state, i, j)
            # Evolve a single cell based on rules
            if cell == 'L' and neighbors == 0:
                next_state[i][j] = '#'
            elif cell == '#' and neighbors >= 5:
                next_state[i][j] = 'L'
    return next_state


def second_count_neighbors(grid, row, col):
    diffs = ((-1, 0), (1,  0), (0, 1), (0, -1),  # North, South, East, West
             (-1, 1), (-1, -1), (1, 1), (1, -1))  # NE, NW, SE, SW
    total = 0
    for diff_row, diff_col in diffs:
        check_row, check_col = row + diff_row, col + diff_col
        while 0 <= check_row <= (len(grid) - 1) and 0 <= check_col <= (len(grid[0]) - 1):
            if grid[check_row][check_col] != '.':
                if grid[check_row][check_col] == '#':
                    total += 1
                break
            check_row += diff_row
            check_col += diff_col
    return total
