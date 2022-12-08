import math
'''
Part One - Consider your map; how many trees are visible from outside the grid?
Part Two - Consider each tree on your map. What is the highest scenic score possible for any tree?
'''


def is_tree_visable(grid, transpose_grid, x, y):
    if x in [0, len(grid) - 1] or y in [0, len(grid[0]) - 1]:
        return True
    tree_value = grid[x][y]
    if max(grid[x][:y]) < tree_value:               # left
        return True
    if max(grid[x][y + 1:]) < tree_value:           # right
        return True
    if max(transpose_grid[y][:x]) < tree_value:     # up
        return True
    if max(transpose_grid[y][x + 1:]) < tree_value:  # down
        return True
    return False


def calculate_scenic_score(grid, transpose_grid, x, y):
    tree_value = grid[x][y]
    scores = [0] * 4
    for tree in reversed(grid[x][:y]):              # left
        scores[0] += 1
        if tree_value <= tree:
            break
    for tree in grid[x][y + 1:]:                    # right
        scores[1] += 1
        if tree_value <= tree:
            break
    for tree in reversed(transpose_grid[y][:x]):    # up
        scores[2] += 1
        if tree_value <= tree:
            break
    for tree in transpose_grid[y][x + 1:]:          # down
        scores[3] += 1
        if tree_value <= tree:
            break
    return math.prod(scores)


def part_one(input):
    grid = [[int(tree) for tree in line] for line in input]
    transpose_grid = [list(x) for x in zip(*grid)]  # Transpose the 2d array
    visable_trees = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if is_tree_visable(grid, transpose_grid, x, y):
                visable_trees += 1
    return visable_trees


def part_two(input):
    grid = [[int(tree) for tree in line] for line in input]
    transpose_grid = [list(x) for x in zip(*grid)]  # Transpose the 2d array
    scenic_scores = []
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            score = calculate_scenic_score(grid, transpose_grid, x, y)
            scenic_scores.append(score)
    return max(scenic_scores)
