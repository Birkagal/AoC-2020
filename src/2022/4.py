import re
''' 
Part One - In how many assignment pairs does one range fully contain the other?
Part Two - In how many assignment pairs do the ranges overlap?
'''


def part_one(input):
    contained_pairs = 0
    for pair in input:
        fstart, fend, sstart, send = map(int, re.findall(
            '[0-9]+', pair
        ))

        start_max = max(fstart, sstart)
        end_min = min(fend, send)

        if (start_max == fstart and end_min == fend) or (start_max == sstart and end_min == send):
            contained_pairs += 1

    return contained_pairs


def part_two(input):
    overlap_pairs = 0
    for pair in input:
        fstart, fend, sstart, send = map(int, re.findall(
            '[0-9]+', pair
        ))

        start_max = max(fstart, sstart)
        end_min = min(fend, send)

        if end_min >= start_max:
            overlap_pairs += 1

    return overlap_pairs
