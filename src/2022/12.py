'''
Part One - What is the fewest steps required to move from your current position to the location that should get the best signal?
Part Two - What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
'''


def get_4neighbors(i, j, h, w):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for di, dj in deltas:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < h and 0 <= new_j < w:
            yield new_i, new_j


def neighbors_forward(grid, i, j, h, w):
    nbors = get_4neighbors(i, j, h, w)

    for new_i, new_j in nbors:
        if ord(grid[new_i][new_j]) <= ord(grid[i][j]) + 1:
            yield new_i, new_j


def neighbors_backward(grid, i, j, h, w):
    nbors = get_4neighbors(i, j, h, w)

    for new_i, new_j in nbors:
        if ord(grid[new_i][new_j]) >= ord(grid[i][j]) - 1:
            yield new_i, new_j


def bfs(grid, src, dst, get_neighbors):
    h, w = len(grid), len(grid[0])
    queue = [(0, src)]
    visited = set()

    while queue:
        distance, coords = queue.pop(0)
        i, j = coords
        if coords == dst or grid[i][j] == dst:
            return distance

        if coords not in visited:
            visited.add(coords)

            for n in get_neighbors(grid, i, j, h, w):
                if n in visited:
                    continue
                queue.append((distance + 1, n))
    return float('inf')


def part_one(input):
    grid = [[*row] for row in input]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                S = i, j
                grid[i][j] = 'a'
            elif grid[i][j] == 'E':
                E = i, j
                grid[i][j] = 'z'

    distance = bfs(grid, S, E, neighbors_forward)
    return distance


def part_two(input):
    grid = [[*row] for row in input]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                grid[i][j] = 'a'
            elif grid[i][j] == 'E':
                E = i, j
                grid[i][j] = 'z'

    distance = bfs(grid, E, 'a', neighbors_backward)
    return distance
