''' 
Part One - Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
Part Two - What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''


def partOne(content):
    return traverse_map(content, 3, 1)


def partTwo(content):
    return traverse_map(content, 1, 1)*traverse_map(content, 3, 1)*traverse_map(content, 5, 1)*traverse_map(content, 7, 1)*traverse_map(content, 1, 2)


# receive a map, and a pattern containing right and down. Traverse the map according the pattern and return amount of threes
def traverse_map(map, right, down):
    trees = 0
    x, y = 0, 0
    y_length = len(map[0])
    x_length = len(map) - 1
    while True:
        if x == x_length:
            return trees
        y = (y+right) % y_length
        x = x + down
        if map[x][y] == '#':
            trees = trees + 1
