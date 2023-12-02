import re
import math

''' 
Part One - Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
Part Two - For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''
pattern = re.compile(r"Game (\d+): (.+)$")


def extract_game_data(game: str) -> tuple[int, str]:
    match = pattern.match(game)
    game_id, colors_part = match.groups()
    colors = re.findall(r'(\d+) (\w+)', colors_part)
    colors = [(int(count), color) for count, color in colors]
    return int(game_id), colors


def part_one(input: list[str]):
    MAX_CUBES = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    possible_game_ids_sum = 0
    for game in input:
        game_id, colors = extract_game_data(game)
        is_possible = True

        for color in colors:
            if color[0] > MAX_CUBES[color[1]]:
                is_possible = False
                break
        if is_possible is True:
            possible_game_ids_sum += game_id

    return possible_game_ids_sum


def part_two(input: list[str]):
    power_set_sum = 0
    for game in input:
        max_cube_colors = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        _, colors = extract_game_data(game)

        for color in colors:
            if color[0] > max_cube_colors[color[1]]:
                max_cube_colors[color[1]] = color[0]
        set_power = math.prod(max_cube_colors.values())
        power_set_sum += set_power

    return power_set_sum
