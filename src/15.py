'''
Part One - Given your starting numbers, what will be the 2020th number spoken?
Part Two - what will be the 30000000th number spoken?
'''


def partOne(content):
    memory = {int(value): [turn+1]
              for turn, value in enumerate(content[0].split(','))}
    last_num = int(content[0].split(',')[-1])
    for turn in range(len(memory)+1, 2020+1):
        if memory.get(last_num, 0) == [(turn-1)]:
            if 0 not in memory:
                memory[0] = [turn]
            else:
                memory[0].append(turn)
            last_num = 0
        else:
            last_num = memory[last_num][-1] - memory[last_num][-2]
            if last_num not in memory:
                memory[last_num] = [turn]
            else:
                memory[last_num].append(turn)
    return last_num


def partTwo(content):
    content = content[0].split(',')
    memory = [0] * 30000000
    last_num = int(content[-1])
    for turn, number in enumerate(content[:-1], 1):
        memory[int(number)] = turn

    for prev_turn in range(len(content), 30000000):
        current_number = prev_turn - memory[last_num]
        if current_number == prev_turn:
            current_number = 0
        memory[last_num] = prev_turn
        last_num = current_number

    return current_number
