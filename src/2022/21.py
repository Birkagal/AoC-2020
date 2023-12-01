''' 
Part One - However, your actual situation involves considerably more monkeys. What number will the monkey named root yell?
Part Two - What number do you yell to pass root's equality test?
'''
OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}


def riddle(monkeys, monkey_name, expected=None):
    monkey = monkeys[monkey_name]
    if isinstance(monkey, int):
        return monkey

    left, op, right = monkey
    left = riddle(monkeys, left)
    right = riddle(monkeys, right)
    op_func = OPERATIONS[op]
    return op_func(left, right)


def sub(monkeys, monkey_name):
    monkey = monkeys[monkey_name]
    if (monkey_name == "humn"):
        return "x"
    if isinstance(monkey, int):
        return monkey
    left, op, right = monkey
    if monkey_name == "root":
        op = "-"
    return f"({sub(monkeys, left)}){op}({sub(monkeys, right)})"


def part_one(input):
    monkeys = {}
    for line in input:
        parts = line.split(' ')
        monkey = parts[0].replace(':', '')
        if len(parts) == 2:
            value = int(parts[1])
            monkeys[monkey] = value
        else:
            left, op, right = parts[1:]
            monkeys[monkey] = (left, op, right)
    ans = riddle(monkeys, 'root')
    return ans


def part_two(input):
    monkeys = {}
    for line in input:
        parts = line.split(' ')
        monkey = parts[0].replace(':', '')
        if len(parts) == 2:
            value = int(parts[1])
            monkeys[monkey] = value
        else:
            left, op, right = parts[1:]
            monkeys[monkey] = (left, op, right)
    ans = sub(monkeys, 'root')

    a, b = [x*100000000000000 for x in [-1, 1]]
    while (True):
        c = (b + a) // 2
        c_res = eval(ans.replace('x', str(c)))
        if (c_res == 0):
            print(c)
            break
        a_res = eval(ans.replace('x', str(a)))
        if (c_res * a_res < 0):
            b = c
        else:
            a = c
    a = 5
