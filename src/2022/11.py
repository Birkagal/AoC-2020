import re
import math
'''
Part One - Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
Part Two - Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
'''


def parse_monkey(monkey_input):
    monkey = {}
    monkey['items'] = list(map(
        int, monkey_input[1].split(': ')[1].split(', ')
    ))
    monkey['operation'] = monkey_input[2].split('= ')[1]
    monkey['test'] = int(re.search('([0-9]+)', monkey_input[3]).group(1))
    monkey['iftrue'] = int(re.search('([0-9]+)', monkey_input[4]).group(1))
    monkey['iffalse'] = int(re.search('([0-9]+)', monkey_input[5]).group(1))
    return monkey


def apply_operation(operation, value):
    left_val = 0
    right_val = 0
    operation_parts = operation.split(' ')

    if operation_parts[0] == 'old':
        left_val = value
    else:
        left_val = int(operation_parts[0])

    if operation_parts[2] == 'old':
        right_val = value
    else:
        right_val = int(operation_parts[2])

    if operation_parts[1] == '+':
        return left_val + right_val
    elif operation_parts[1] == '*':
        return left_val * right_val
    elif operation_parts[1] == '-':
        return left_val - right_val
    elif operation_parts[1] == '/':
        return left_val // right_val


def monkey_turn(
    monkey,
    monkey_index,
    monkeys_items,
    monkeys_inspections,
    supermod,
    shrink_factor=1
):
    # Copy of list, because we need to remove
    for item in monkeys_items[monkey_index][:]:
        monkeys_inspections[monkey_index] += 1
        monkeys_items[monkey_index].pop(0)
        new_value = apply_operation(monkey['operation'], item)
        new_value %= supermod
        new_value //= shrink_factor
        divisibility_value = monkey['test']
        if new_value % divisibility_value == 0:
            new_monkey_idx = monkey['iftrue']
        else:
            new_monkey_idx = monkey['iffalse']
        monkeys_items[new_monkey_idx].append(new_value)


def part_one(input):
    monkeys = []
    monkeys_items = []
    monkeys_inspections = []

    for index in range(0, len(input), 7):
        monkey = parse_monkey(input[index:index + 6])
        monkeys.append(monkey)
        monkeys_items.append(monkey['items'])
        monkeys_inspections.append(0)

    supermod = math.lcm(*(monkey['test'] for monkey in monkeys))

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            monkey_turn(
                monkey, i, monkeys_items, monkeys_inspections, supermod, shrink_factor=3
            )
    return math.prod(sorted(monkeys_inspections, reverse=True)[:2])


def part_two(input):
    monkeys = []
    monkeys_items = []
    monkeys_inspections = []
    for index in range(0, len(input), 7):
        monkey = parse_monkey(input[index:index + 6])
        monkeys.append(monkey)
        monkeys_items.append(monkey['items'])
        monkeys_inspections.append(0)

    supermod = math.lcm(*(monkey['test'] for monkey in monkeys))

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            monkey_turn(
                monkey, i, monkeys_items, monkeys_inspections, supermod
            )
    return math.prod(sorted(monkeys_inspections, reverse=True)[:2])
