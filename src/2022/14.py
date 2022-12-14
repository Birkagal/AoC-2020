from operator import itemgetter
''' 
Part One - Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
Part Two - Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
'''


def drop_sand(taken, floor_y, fill=False):
    point = (500, 0)

    if fill and point in taken:
        return False

    while True:
        x, y = point
        y += 1

        if y == floor_y:
            if fill:
                taken.add(point)
            return fill

        if (x, y) not in taken:
            point = (x, y)
            continue
        if (x - 1, y) not in taken:
            point = (x - 1, y)
            continue
        if (x + 1, y) not in taken:
            point = (x + 1, y)
            continue

        taken.add(point)
        return True


def get_rocks(input):
    lines = [
        [
            tuple(map(int, point.split(',')))
            for point in row.replace(' ', '').split('->')
        ]
        for row in input
    ]

    rocks = set()
    for line in lines:
        p_x, p_y = line[0]
        for (n_x, n_y) in line[1:]:
            if p_x == n_x:
                start_y, end_y = min([p_y, n_y]), max([p_y, n_y])
                line_points = [(n_x, y) for y in range(start_y, end_y + 1)]
            else:
                start_x, end_x = min([p_x, n_x]), max([p_x, n_x])
                line_points = [(x, n_y) for x in range(start_x, end_x + 1)]
            rocks.update(line_points)
            p_x, p_y = n_x, n_y
    return rocks


def part_one(input):
    taken = get_rocks(input)
    floor_y = max(map(itemgetter(1), taken)) + 1
    ans = 0
    while drop_sand(taken, floor_y):
        ans += 1
    return ans


def part_two(input):
    taken = get_rocks(input)
    floor_y = max(map(itemgetter(1), taken)) + 2
    ans = 0
    while drop_sand(taken, floor_y, fill=True):
        ans += 1
    return ans
