from operator import itemgetter
from itertools import count
'''
Part One - How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
Part Two - How tall will the tower be after 1000000000000 rocks have stopped?
'''

ROCK_TYPES = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1))
]


def newrock(off, topy):
    r = []
    for dx, dy in off:
        r.append([dx + 2, (topy + dy + 4)])
    return r


def collision(rock, direction, space):
    if direction == 'l':
        if any(x == 0 for x, _ in rock):
            return True
        for x, y in rock:
            if (x - 1, y) in space:
                return True

    elif direction == 'r':
        if any(x == 6 for x, _ in rock):
            return True
        for x, y in rock:
            if (x + 1, y) in space:
                return True

    elif direction == 'd':
        if any(y == 1 for _, y in rock):
            return True
        for x, y in rock:
            if (x, y - 1) in space:
                return True

    return False


def part_one(input):
    topy = 0
    space = {(i, 0) for i in range(7)}
    moves = (input[0][i % len(input[0])] for i in count(0))

    for n in range(2022):
        rocktype = n % len(ROCK_TYPES)
        rock = newrock(ROCK_TYPES[rocktype], topy)

        while 1:
            move = next(moves)

            if move == '<' and not collision(rock, 'l', space):
                for i, (x, y) in enumerate(rock):
                    rock[i] = (x - 1, y)
            elif move == '>' and not collision(rock, 'r', space):
                for i, (x, y) in enumerate(rock):
                    rock[i] = (x + 1, y)

            if collision(rock, 'd', space):
                space.update(map(tuple, rock))
                topy = max(map(itemgetter(1), space))
                break

            # Down
            for i, (x, y) in enumerate(rock):
                rock[i] = (x, y - 1)

    return topy


def part_two(input):
    topy = 0
    space = {(i, 0) for i in range(7)}
    moves = (input[0][i % len(input[0])] for i in count(0))
    previous = {}
    n_rocks = 0
    skipped = None
    totrocks = 1_000_000_000_000

    while n_rocks < totrocks:
        rocktype = n_rocks % len(ROCK_TYPES)
        rock = newrock(ROCK_TYPES[rocktype], topy)

        while 1:
            move = next(moves)

            if move == '<' and not collision(rock, 'l', space):
                for i, (x, y) in enumerate(rock):
                    rock[i] = (x - 1, y)

            elif move == '>' and not collision(rock, 'r', space):
                for i, (x, y) in enumerate(rock):
                    rock[i] = (x + 1, y)

            if collision(rock, 'd', space):
                space.update(map(tuple, rock))
                topy = max(map(itemgetter(1), space))

                if skipped is None and topy > 200:
                    topchunk = []
                    for x, y in space:
                        if y >= topy - 100:
                            topchunk.append((x, topy - y))

                    state = (tuple(sorted(topchunk)), rocktype)

                    if state in previous:
                        nn, yy = previous[state]
                        deltay = topy - yy
                        deltan = n_rocks - nn
                        steps = (totrocks - n_rocks) // deltan
                        skipped = deltay * steps
                        n_rocks += deltan * steps

                    previous[state] = (n_rocks, topy)

                break

            # Down
            for i, (x, y) in enumerate(rock):
                rock[i] = (x, y - 1)

        n_rocks += 1

    return topy + skipped
