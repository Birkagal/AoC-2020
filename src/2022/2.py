''' 
Part One - What would your total score be if everything goes exactly according to your strategy guide?
Part Two - Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''


def simulate_games(games: list, rps_map: dict):
    return [
        rps_map[game.split(' ')[0]][game.split(' ')[1]]
        for game in games
    ]


def part_one(input):
    rps_map = {
        'A': {
            'X': 4,
            'Y': 8,
            'Z': 3,
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C': {
            'X': 7,
            'Y': 2,
            'Z': 6,
        }
    }
    return sum(simulate_games(input, rps_map))


def part_two(input):
    rps_map = {
        'A': {
            'X': 3,
            'Y': 4,
            'Z': 8,
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9,
        },
        'C': {
            'X': 2,
            'Y': 6,
            'Z': 7,
        }
    }
    return sum(simulate_games(input, rps_map))
