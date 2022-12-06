from collections import deque
''' 
Part One - How many characters need to be processed before the first start-of-packet marker is detected?
Part Two - 
'''


def find_unique_values(input, amount):
    l = deque(maxlen=amount)
    for index, char in enumerate(input[0]):
        l.append(char)
        if len(l) != amount:
            continue
        seen = set()
        if not any(i in seen or seen.add(i) for i in l):
            return index + 1
    return -1


def part_one(input):
    return find_unique_values(input, 4)


def part_two(input):
    return find_unique_values(input, 14)
