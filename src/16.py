from math import prod
'''
Part One - Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
Part Two - look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?
'''


class CustomRange:
    def __init__(self, first_range, sencond_range):
        self.a, self.b, self.c, self.d = first_range[0], first_range[1], sencond_range[0], sencond_range[1]

    def __contains__(self, value):
        return self.a <= value <= self.b or self.c <= value <= self.d


def parse_data(data):
    index = 0
    for i, line in enumerate(data):
        if line == '':
            index = i
            break

    constraints_data = data[:index]
    my_ticket = list(map(int, data[index+2].split(',')))
    tickets_data = [list(map(int, ticket.split(',')))
                    for ticket in data[(index+5):]]

    constraints = []
    for constraint in constraints_data:
        current_line = constraint.split(':')[1].split()
        first = [int(number) for number in current_line[0].split('-')]
        second = [int(number) for number in current_line[2].split('-')]
        constraints.append(CustomRange(first, second))
    return constraints, my_ticket, tickets_data


def validate_number(value, constraints):
    for constraint in constraints:
        if value in constraint:
            return True
    return False


def partOne(content):
    constraints, my_ticket, tickets_data = parse_data(content)
    return sum(sum([[number for number in ticket if not validate_number(
        number, constraints)] for ticket in tickets_data], []))


def validate_ticket(ticket, constraints):
    return all(any(value in rng for rng in constraints) for value in ticket)


def get_corrent_indexes(possible):
    found = [None] * len(possible)
    while any(possible):
        for i, option in enumerate(possible):
            if len(option) == 1:
                found[i] = option.pop()
                break
        for other in possible:
            if found[i] in other:
                other.remove(found[i])
    return found


def partTwo(content):
    constraints, my_ticket, tickets = parse_data(content)
    tickets.append(my_ticket)
    num_of_field = len(my_ticket)
    possible = [set(range(num_of_field)) for _ in range(num_of_field)]

    for ticket in tickets:
        if validate_ticket(ticket, constraints):
            for rng, option in zip(constraints, possible):
                for index, value in enumerate(ticket):
                    if value not in rng and index in option:
                        option.remove(index)

    corrent_indexes = get_corrent_indexes(possible)
    return prod([my_ticket[corrent_indexes[i]] for i in range(6)])
