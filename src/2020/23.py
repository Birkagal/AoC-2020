'''
Part One - Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?
Part Two - Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?
'''


def play_game(next_cup, starting_cup, n_turns):
    max_cup = max(next_cup)
    cur = starting_cup

    for _ in range(n_turns):
        # Pick up 3 cups
        first = next_cup[cur]
        mid = next_cup[first]
        last = next_cup[mid]
        picked = (first, mid, last)

        # Remove them from the list
        next_cup[cur] = next_cup[last]

        # Select the destination cup value, after which we'll insert the 3 picked-up cups
        dst = max_cup if cur == 1 else cur - 1
        while dst in picked:
            dst = max_cup if dst == 1 else dst - 1

        # Insert the picked cups right after it
        next_cup[last] = next_cup[dst]
        next_cup[dst] = first

        # Advance to the next cup after the current
        cur = next_cup[cur]
    return next_cup


def create_next_list(cups, size):
    next_cup = [0] * (len(cups)+1)

    for prev, cur in zip(cups, cups[1:]):
        next_cup[prev] = cur
    if size == (len(cups)+1):
        next_cup[cups[-1]] = cups[0]
    else:
        next_cup += list(range(len(cups) + 2, size + 2))
        next_cup[cups[-1]] = len(cups)+1
        next_cup[-1] = cups[0]
    return next_cup


def part_one(content):
    cups = [int(num) for num in content[0]]
    next_cup = create_next_list(cups, 10)
    play_game(next_cup, cups[0], 100)

    ans = ''
    current = 1
    for _ in range(8):
        current = next_cup[current]
        ans += str(current)
    return ans


def part_two(content):
    cups = [int(num) for num in content[0]]
    next_cup = create_next_list(cups, 1000000)
    play_game(next_cup, cups[0], 10000000)
    return next_cup[1] * next_cup[next_cup[1]]
