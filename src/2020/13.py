from functools import reduce
''' 
Part One - What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
Part Two - What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
'''


def part_one(content):
    estimate_time = int(content[0])
    bus_list = [int(bus_id)
                for bus_id in content[1].split(',') if bus_id != 'x']
    buses_with_time = []
    best_bus = []
    for bus in bus_list:
        waiting_time = bus - (estimate_time % bus)
        buses_with_time.append([bus, waiting_time])
    best_bus = buses_with_time[0]
    for bus_with_time in buses_with_time:
        if bus_with_time[1] < best_bus[1]:
            best_bus = bus_with_time
    return best_bus[0] * best_bus[1]


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def part_two(content):
    buses = [(i, int(bus))
             for i, bus in enumerate(content[1].split(',')) if bus != 'x']
    dividers = [bus for _, bus in buses]
    remainders = [bus - i for i, bus in buses]
    return chinese_remainder(dividers, remainders)
