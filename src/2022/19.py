import re
from collections import deque
''' 
Part One - Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. What do you get if you add up the quality level of all of the blueprints in your list?
Part Two - Don't worry about quality levels; instead, just determine the largest number of geodes you could open using each of the first three blueprints. What do you get if you multiply these numbers together?
'''


def best_case_scenario(initial_amount, robots, t):
    return initial_amount + robots * (t + 1) + t * (t + 1) // 2


def dfs(blueprint, time=24):
    ORE, CLAY, OBS, GEO = range(4)
    rore_cost, rclay_cost, robs_cost_ore, robs_cost_clay, rgeo_cost_ore, rgeo_cost_obs = blueprint
    max_ore_needed = max(rore_cost, rclay_cost, robs_cost_ore, rgeo_cost_ore)
    max_clay_needed = robs_cost_clay
    max_obs_needed = rgeo_cost_obs

    best = 0
    visited = set()
    q = deque([(time, 0, 0, 0, 0, 1, 0, 0, 0, ())])

    while q:
        tmp = q.pop()

        state = tmp[:-1]
        if state in visited:
            continue

        visited.add(state)

        time, ore, clay, obs, geo, rore, rclay, robs, rgeo, did_not_build = tmp
        newore = ore + rore
        newclay = clay + rclay
        newobs = obs + robs
        newgeo = geo + rgeo
        time -= 1

        if time == 0:
            best = max(best, newgeo)
            continue

        if best_case_scenario(newgeo, rgeo, time) < best:
            continue

        if best_case_scenario(newobs, robs, time) < rgeo_cost_obs \
                or best_case_scenario(newore, rore, time) < rgeo_cost_ore:
            best = max(best, newgeo + rgeo * time)
            continue

        can_build = []

        if obs >= rgeo_cost_obs and ore >= rgeo_cost_ore and GEO not in did_not_build:
            can_build.append(GEO)
            q.append((time, newore - rgeo_cost_ore, newclay, newobs -
                     rgeo_cost_obs, newgeo, rore, rclay, robs, rgeo + 1, ()))

        if robs < max_obs_needed and clay >= robs_cost_clay and ore >= robs_cost_ore and OBS not in did_not_build:
            can_build.append(OBS)
            q.append((time, newore - robs_cost_ore, newclay - robs_cost_clay,
                     newobs, newgeo, rore, rclay, robs + 1, rgeo, ()))

        if rclay < max_clay_needed and ore >= rclay_cost and CLAY not in did_not_build:
            can_build.append(CLAY)
            q.append((time, newore - rclay_cost, newclay, newobs,
                     newgeo, rore, rclay + 1, robs, rgeo, ()))

        if rore < max_ore_needed and ore >= rore_cost and ORE not in did_not_build:
            can_build.append(ORE)
            q.append((time, newore - rore_cost, newclay, newobs,
                     newgeo, rore + 1, rclay, robs, rgeo, ()))

        if (robs and obs < max_obs_needed) or (rclay and clay < max_clay_needed) or ore < max_ore_needed:
            q.append((time, newore, newclay, newobs, newgeo,
                     rore, rclay, robs, rgeo, can_build))

    return best


def parse_blueprints(input):
    blueprints = []
    for line in input:
        data = tuple(map(int, re.findall('\d+', line)))
        blueprints.append(data)
    return blueprints


def part_one(input):
    blueprints = parse_blueprints(input)
    total = 0
    for bid, *blueprint in blueprints:
        total += bid * dfs(blueprint)
    return total


def part_two(input):
    blueprints = parse_blueprints(input[:3])
    total = 1
    for bid, *blueprint in blueprints:
        total *= dfs(blueprint, time=32)
    return total
