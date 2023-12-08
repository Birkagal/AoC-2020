from functools import cmp_to_key
from collections import defaultdict
from enum import Enum
''' 
Part One - Find the rank of every hand in your set. What are the total winnings?
Part Two - Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
'''


class HandValues(Enum):
    FiveOfKind = 6
    FourOfKind = 5
    FullHouse = 4
    ThreeOfKind = 3
    TwoPair = 2
    Pair = 1
    HighCard = 0


CARD_RANKS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}
CARD_RANKS_WITH_JOKER = dict(CARD_RANKS)
CARD_RANKS_WITH_JOKER['J'] = 1


def get_hand_rank(hand_labels: dict[str, int], is_jokers: bool = False) -> HandValues:
    hand_js = hand_labels.pop('J', 0) if is_jokers is True else 0
    hand_values = list(hand_labels.values())
    if is_jokers is True:
        hand_labels['J'] = hand_js
    max_label = max(hand_values) + hand_js if hand_values else 5

    match max_label:
        case 5:
            return HandValues.FiveOfKind
        case 4:
            return HandValues.FourOfKind
        case 3:
            if len(hand_values) == 2:
                return HandValues.FullHouse
            else:
                return HandValues.ThreeOfKind
        case 2:
            if len(hand_values) == 3:
                return HandValues.TwoPair
            else:
                return HandValues.Pair
        case 1:
            return HandValues.HighCard

def compare_hands(hand1, hand2, is_jokers=False):
    hand1 = hand1.split()[0]
    hand2 = hand2.split()[0]
    hand1_labels = defaultdict(int)
    hand2_labels = defaultdict(int)
    for c in hand1:
        hand1_labels[c] += 1

    for c in hand2:
        hand2_labels[c] += 1

    hand1_rank = get_hand_rank(hand1_labels, is_jokers)
    hand2_rank = get_hand_rank(hand2_labels, is_jokers)

    if hand1_rank == hand2_rank:
        for c1, c2 in zip(hand1, hand2):
            c1_rank, c2_rank = CARD_RANKS[c1], CARD_RANKS[c2]
            if is_jokers is True and c1 == 'J':
                c1_rank = 1
            if is_jokers is True and c2 == 'J':
                c2_rank = 1
            if c1_rank != c2_rank:
                return c2_rank - c1_rank

    return hand2_rank.value - hand1_rank.value


def cmp_with_jokers(hand1, hand2):
    return compare_hands(hand1, hand2, is_jokers=True)


def part_one(input: list[str]) -> int:
    total_winnings = 0
    ordered_hands = sorted(input, key=cmp_to_key(compare_hands), reverse=True)

    for rank, hand in enumerate(ordered_hands):
        bid = int(hand.split()[1])
        total_winnings += bid * (rank + 1)

    return total_winnings


def part_two(input: list[str]) -> int:
    total_winnings = 0
    ordered_hands = sorted(input, key=cmp_to_key(cmp_with_jokers), reverse=True)

    for rank, hand in enumerate(ordered_hands):
        bid = int(hand.split()[1])
        total_winnings += bid * (rank + 1)

    return total_winnings
