import json
from functools import cmp_to_key
'''
Part One - Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
Part Two - Organize all of the packets into the correct order. What is the decoder key for the distress signal?
'''


def cmp(left, right):
    is_left_int, is_right_int = isinstance(left, int), isinstance(right, int)

    if is_left_int and is_right_int:
        return right - left

    if is_left_int or is_right_int:
        if is_left_int:
            return cmp([left], right)
        else:
            return cmp(left, [right])

    for l, r in zip(left, right):
        res = cmp(l, r)
        if res != 0:
            return res

    return len(right) - len(left)


def part_one(input):
    input = [line for line in input if line != '']
    packets = list(map(json.loads, input))
    pairs = [packets[i:i + 2] for i in range(0, len(packets), 2)]
    result = sum((
        index for index, (left, right) in enumerate(pairs, 1)
        if cmp(left, right) > 0
    ))
    return result


def part_two(input):
    input = [line for line in input if line != '']
    packets = list(map(json.loads, input))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(cmp), reverse=True)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
