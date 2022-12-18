import re
'''
Part One - Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?
Part Two - Find the only possible position for the distress beacon. What is its tuning frequency?
'''


def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


def part_one(input):
    TARGET_Y = 2_000_000
    taken = set()
    utilities = set()
    for line in input:
        s_x, s_y, b_x, b_y = map(int, re.findall('-?\d+', line))
        sensor, beacon = (s_x, s_y), (b_x, b_y)
        if b_y == TARGET_Y:
            utilities.add(b_x)
        distance = manhattan(sensor, beacon)

        right = s_x + distance
        left = s_x - distance
        down = s_y + distance
        up = s_y - distance

        if up <= TARGET_Y <= down:
            delta = abs(TARGET_Y - s_y)
            rang = range(left + delta, right - delta + 1)
            taken.update(rang)

    return len(taken - utilities)


def part_two(input):
    MIN, MAX = 0, 4_000_000
    sensors = []
    for line in input:
        s_x, s_y, b_x, b_y = map(int, re.findall('-?\d+', line))
        sensors.append((s_x, s_y, b_x, b_y))

    for y in range(MAX + 1):
        segments = []
        for sensor in sensors:
            s_x, s_y, b_x, b_y = sensor
            distance = manhattan((s_x, s_y), (b_x, b_y))

            right = s_x + distance
            left = s_x - distance
            down = s_y + distance
            up = s_y - distance

            if up <= y <= down:
                delta = abs(y - s_y)
                start = max(MIN, left + delta)
                end = min(right - delta + 1, MAX)
                segments.append((start, end))

        segments.sort()
        best_end = segments[0][1]
        for start, end in segments[1:]:
            if start <= best_end:
                best_end = max(best_end, end)
            else:
                return (start - 1) * MAX + y

    return -1
