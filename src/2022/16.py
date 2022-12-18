
import re
from math import inf as INFINITY
from itertools import product, combinations
from collections import defaultdict
''' 
Part One - Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?
Part Two - With you and an elephant working together for 26 minutes, what is the most pressure you could release?
'''


def parse_valves(input):
    valves = {}
    for line in input:
        r = re.search(
            'Valve ([A-Z]+) has flow rate=(\d+);[a-z ]+([A-Z]+.+)', line
        )
        valve, flowrate, path = r.group(1), r.group(2), r.group(3)
        paths = path.replace(' ', '').split(',')
        valves[valve] = {
            'flowrate': int(flowrate),
            'paths': paths,
        }
    return valves


def floyd_warshall(valves):
    distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

    for src in valves.keys():
        paths = valves[src]['paths']
        distance[src][src] = 0

        for path in paths:
            distance[path][path] = 0
            distance[src][path] = 1

    for a, b, c in product(valves, valves, valves):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance


def solutions(distance, valves, time=30, cur='AA', chosen={}):
    for nxt in valves:
        new_time = time - (distance[cur][nxt] + 1)
        if time < 2:
            continue
        new_chosen = chosen | {nxt: new_time}
        new_valves = valves - {nxt}
        yield from solutions(distance, new_valves, new_time, nxt, new_chosen)
    yield chosen


def score(valves, chosen_valves):
    return sum((
        valves[valve]['flowrate'] * time_left for valve, time_left in chosen_valves.items()
    ))


def part_one(input):
    valves = parse_valves(input)
    distance = floyd_warshall(valves)
    nonzero_valves = set(filter(lambda v: valves[v]['flowrate'] > 0, valves))

    best = max(
        score(valves, sol)
        for sol in solutions(distance, nonzero_valves)
    )
    return best


def part_two(input):
    valves = parse_valves(input)
    distance = floyd_warshall(valves)
    nonzero_valves = set(filter(lambda v: valves[v]['flowrate'] > 0, valves))

    maxscore = defaultdict(int)

    for solution in solutions(distance, nonzero_valves, 26):
        k = frozenset(solution)
        s = score(valves, solution)

        if s > maxscore[k]:
            maxscore[k] = s

    best = max(sa + sb for (a, sa), (b, sb)
               in combinations(maxscore.items(), 2) if not a & b)
    return best
