from collections import deque
'''
Part One - Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
Part Two - Play the small crab in a game of Recursive Combat using the same two decks as before. What is the winning player's score?
'''


def parse_data(data):
    p1_deck, p2_deck = [], []
    into_p1 = True
    for line in data[1:]:
        if line == '':
            continue
        if line == 'Player 2:':
            into_p1 = False
        else:
            if into_p1:
                p1_deck.append(int(line))
            else:
                p2_deck.append(int(line))
    return p1_deck, p2_deck


def play_combat(p1_deck, p2_deck):
    while True:
        card1, card2 = p1_deck.pop(0), p2_deck.pop(0)
        if card1 > card2:
            p1_deck += [card1, card2]
        else:
            p2_deck += [card2, card1]
        if p1_deck == []:
            return p2_deck
        if p2_deck == []:
            return p1_deck


def recursive_combat(p1_deck, p2_deck):
    seen = set()

    while p1_deck and p2_deck:
        key = tuple(p1_deck), tuple(p2_deck)
        if key in seen:
            return True, p1_deck

        seen.add(key)
        card1, card2 = p1_deck.pop(0), p2_deck.pop(0)

        if len(p1_deck) >= card1 and len(p2_deck) >= card2:
            sub1, sub2 = tuple(p1_deck)[:card1], tuple(p2_deck)[:card2]
            p1win, _ = recursive_combat(list(sub1), list(sub2))
        else:
            p1win = card1 > card2

        if p1win:
            p1_deck += [card1, card2]
        else:
            p2_deck += [card2, card1]

    return (True, p1_deck) if p1_deck else (False, p2_deck)


def partOne(content):
    p1_deck, p2_deck = parse_data(content)
    winner_deck = play_combat(p1_deck, p2_deck)
    return sum([(i+1)*card for i, card in enumerate(winner_deck[::-1])])


def partTwo(content):
    p1_deck, p2_deck = parse_data(content)
    _, winner_deck = recursive_combat(p1_deck, p2_deck)
    return sum([(i+1)*card for i, card in enumerate(winner_deck[::-1])])
