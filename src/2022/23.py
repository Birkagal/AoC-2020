from collections import deque, defaultdict
from operator import itemgetter
from itertools import count
''' 
Part One - 
Part Two - 
'''


MOVES = deque([
    ((-1, 0), (-1, 1), (-1, -1), (-1, 0)),
    ((1, 0), (1, 1), (1, -1), (1, 0)),
    ((0, -1), (-1, -1), (1, -1), (0, -1)),
    ((0, 1), (-1, 1), (1, 1), (0, 1)),
])


def move(grid, r, c):
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        if (r + dr, c + dc) in grid:
            break
    else:
        return

    for *deltas, want in MOVES:
        good = True
        for dr, dc in deltas:
            rr, cc = r + dr, c + dc
            if (rr, cc) in grid:
                good = False
                break

        dr, dc = want
        if good:
            rr, cc = r + dr, c + dc
            return rr, cc


def sim(grid):
    newg = set()
    nextpos = {}
    propcount = defaultdict(int)

    for r, c in grid:
        dst = move(grid, r, c)
        if dst is None:
            nextpos[r, c] = (r, c)
        else:
            propcount[dst] += 1
            nextpos[r, c] = dst

    for pos, newpos in nextpos.items():
        if propcount[newpos] == 1:
            r, c = newpos
            newg.add((r, c))
        else:
            r, c = pos
            newg.add((r, c))

    MOVES.rotate(-1)
    return newg


def part_one(input):
    grid = set()
    for r, row in enumerate(input):
        for c, cell in enumerate(row):
            if cell == '#':
                grid.add((r, c))

    for i in range(1, 10 + 1):
        grid = sim(grid)

    rmin, rmax = min(map(itemgetter(0), grid)), max(map(itemgetter(0), grid))
    cmin, cmax = min(map(itemgetter(1), grid)), max(map(itemgetter(1), grid))

    ans = 0
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if (r, c) not in grid:
                ans += 1
    return ans


def part_two(input):
    grid = set()
    for r, row in enumerate(input):
        for c, cell in enumerate(row):
            if cell == '#':
                grid.add((r, c))

    for ans in count():
        old = grid
        grid = sim(grid)
        if grid == old:
            break
    return ans
