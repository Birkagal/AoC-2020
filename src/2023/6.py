import re
import math
''' 
Part One - Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?
Part Two - How many ways can you beat the record in this one much longer race?
'''


def count_possible_wins(time: int, record: int) -> int:
    possible_wins = 0
    for i in range(1, time + 1):
        current_score = i * (time - i)
        if current_score > record:
            possible_wins += 1
    return possible_wins


def part_one(input: list[str]) -> int:
    times = map(int, re.findall(r'\d+', input[0]))
    record_dists = map(int, re.findall(r'\d+', input[1]))
    possible_wins = []
    
    for time, record in zip(times, record_dists):
        wins_count = count_possible_wins(time, record)
        possible_wins.append(wins_count)

    return math.prod(possible_wins)


def part_two(input: list[str]) -> int:
    time = int(''.join(re.findall(r'\d+', input[0])))
    record = int(''.join(re.findall(r'\d+', input[1])))
    wins_count = count_possible_wins(time, record)
    return wins_count
