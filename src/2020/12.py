import numpy as np
''' 
Part One - What is the Manhattan distance between that location and the ship's starting position?
Part Two - Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?
'''


def parse_content(content):
    directions = []
    for line in content:
        char = line[0]
        value = int(line[1:])
        directions.append((char, value))
    return directions


def part_one(content):
    directions = parse_content(content)
    nesw = [0, 0, 0, 0]
    current_position = 1
    for direction in directions:
        action = direction[0]
        value = int(direction[1])
        if action == 'N':
            nesw[0] += value
        elif action == 'S':
            nesw[2] += value
        elif action == 'E':
            nesw[1] += value
        elif action == 'W':
            nesw[3] += value
        elif action == 'L':
            current_position = (current_position - (value//90)) % 4
        elif action == 'R':
            current_position = (current_position + (value//90)) % 4
        elif action == 'F':
            nesw[current_position] += value
    return abs(nesw[1]-nesw[3]) + abs(nesw[2]-nesw[0])


def part_two(content):
    directions = parse_content(content)
    nesw = [0, 0, 0, 0]
    waypoint = [1, 10, 0, 0]
    for direction in directions:
        action = direction[0]
        value = int(direction[1])
        if action == 'N':
            waypoint[0] += value
        elif action == 'S':
            waypoint[2] += value
        elif action == 'E':
            waypoint[1] += value
        elif action == 'W':
            waypoint[3] += value
        elif action == 'L':
            waypoint = np.roll(waypoint, -value//90)
        elif action == 'R':
            waypoint = np.roll(waypoint, value//90)
        elif action == 'F':
            nesw[0] += value*waypoint[0]
            nesw[1] += value*waypoint[1]
            nesw[2] += value*waypoint[2]
            nesw[3] += value*waypoint[3]
    return abs(nesw[1]-nesw[3]) + abs(nesw[2]-nesw[0])
