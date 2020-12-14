import copy
''' 
Part One - Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
Part Two - Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
'''


def get_neigbors(state, i, j):
    neighbors = 0
    num_rows = len(state) - 1
    num_cols = len(state[0]) - 1
    while j != num_cols:
        if state[i][j+1] == '.':
            j += 1
        if state[i][j+1] == '#':
            neighbors += 1
            break
        if state[i][j+1] == 'L':
            break
    if j != num_cols:
        if state[i][j+1] == '#':
            neighbors += 1
        if i != 0 and state[i-1][j+1] == '#':
            neighbors += 1
        if i != num_rows and state[i+1][j+1] == '#':
            neighbors += 1
    if j != 0:
        if state[i][j-1] == '#':
            neighbors += 1
        if i != 0 and state[i-1][j-1] == '#':
            neighbors += 1
        if i != num_rows and state[i+1][j-1] == '#':
            neighbors += 1
    if i != 0 and state[i-1][j] == '#':
        neighbors += 1
    if i != num_rows and state[i+1][j] == '#':
        neighbors += 1
    return neighbors


def play_turn(state):
    next_state = copy.deepcopy(state)
    for i, line in enumerate(state):
        for j, char in enumerate(line):
            if char == '.':
                continue
            neighbors = get_neigbors(state, i, j)
            if char == 'L' and neighbors == 0:
                next_state[i][j] = '#'
            elif char == '#' and neighbors >= 4:
                next_state[i][j] = 'L'
    return next_state


def count_seats(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '#':
                count += 1
    return count


# def partOne(content):
#     state = [list(line) for line in content]
#     next_state = play_turn(state)
#     tmp_state = []
#     while state != next_state:
#         tmp_state = copy.deepcopy(next_state)
#         next_state = play_turn(next_state)
#         state = copy.deepcopy(tmp_state)
#     return count_seats(state)


def partTwo(data):
    state = [list(line) for line in data]
    next_state = play_turn(state)
    tmp_state = []
    while state != next_state:
        tmp_state = copy.deepcopy(next_state)
        next_state = play_turn(next_state)
        state = copy.deepcopy(tmp_state)
    return count_seats(state)
