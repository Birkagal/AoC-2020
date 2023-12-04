import re
from collections import defaultdict

''' 
Part One - Take a seat in the large pile of colorful cards. How many points are they worth in total?
Part Two - Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?
'''
pattern = re.compile(r"Card\s+(\d+):\s+(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)")


def part_one(input: list[str]):
    total = 0

    for game in input:
        _, winnings, numbers = pattern.match(game).groups()
        winnings = set(map(int, winnings.split()))
        numbers = list(map(int, numbers.split()))
        num_winning_cards = 0

        for n in numbers:
            if n in winnings:
                num_winning_cards += 1

        if num_winning_cards > 0:
            total += 2 ** (num_winning_cards - 1)

    return total


def part_two(input: list[str]):
    copies = defaultdict(lambda: 1)
    copies[1] = 1

    for game in input:
        game_id, winnings, numbers = pattern.match(game).groups()
        game_id = int(game_id)
        winnings = set(map(int, winnings.split()))
        numbers = list(map(int, numbers.split()))
        num_winning_cards = 0

        for n in numbers:
            if n in winnings:
                num_winning_cards += 1

        if game_id not in copies:
            copies[game_id] = 1
        for _ in range(copies[game_id]):
            for id in range(game_id, game_id + num_winning_cards):
                copies[id + 1] += 1

    return sum(copies.values())
