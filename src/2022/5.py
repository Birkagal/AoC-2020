import re
'''
Part One - After the rearrangement procedure completes, what crate ends up on top of each stack?
Part Two - Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
'''


def parse_stacks(input, input_break_index):
    stacks = [[] for _ in range(9)]
    for line in input[:input_break_index - 1]:
        for i in range(0, len(line), 4):
            crate = line[i:i+4]
            if crate[0] != ' ':
                stacks[i // 4].append(crate[1])
    return stacks


def part_one(input):
    input_break_index = input.index('')
    stacks = parse_stacks(input, input_break_index)
    for move in input[input_break_index + 1:]:
        amount, src, dst = map(int, re.findall('[0-9]+', move))
        stacks[dst - 1] = list(reversed(
            stacks[src - 1][:amount]
        )) + stacks[dst - 1]
        stacks[src - 1] = stacks[src - 1][amount:]
    return ''.join(stack[0] for stack in stacks)


def part_two(input):
    input_break_index = input.index('')
    stacks = parse_stacks(input, input_break_index)
    for move in input[input_break_index + 1:]:
        amount, src, dst = map(int, re.findall('[0-9]+', move))
        stacks[dst - 1] = stacks[src - 1][:amount] + stacks[dst - 1]
        stacks[src - 1] = stacks[src - 1][amount:]
    return ''.join(stack[0] for stack in stacks)
