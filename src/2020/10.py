from functools import lru_cache

''' 
Part One - What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
Part Two - What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
'''


def part_one(content):
    adapters = sorted([int(adapter) for adapter in content])
    adapters.append(int(content[-1])+3)
    diff1 = diff3 = 1
    for current, nxt in zip(adapters, adapters[1:]):
        diff = nxt - current
        if diff == 1:
            diff1 += 1
        if diff == 3:
            diff3 += 1
    return diff1*diff3


def part_two(content):
    adapters = sorted([int(adapter) for adapter in content])
    adapters = [0] + adapters + [max(adapters)+3]
    return solve_with_cache(adapters, 0)


def solve_with_cache(adapters, index):
    # Decorate using lru_cache() without the first parameter
    @lru_cache()
    def find_all_possibles_from(index):
        nonlocal adapters
        if index == len(adapters) - 1:
            return 1
        tot = 0
        for j in range(index + 1, min(index + 4, len(adapters))):
            if adapters[j] - adapters[index] <= 3:
                tot += find_all_possibles_from(j)
        return tot
    # Do the actual initial call passing only the second parameter
    return find_all_possibles_from(index)
