''' 
Part One - Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
Part Two - Render the image given by your program. What eight capital letters appear on your CRT?
'''


def part_one(input):
    cycle = 1
    register = 1
    signal = 0
    for command in input:
        cycle += 1
        command = command.split(' ')
        if command[0] == 'addx':
            if cycle % 40 == 20:
                signal += cycle * register
            cycle += 1
            register += int(command[1])
        if cycle % 40 == 20:
            signal += cycle * register
    return signal


def part_two(input):
    cycle = 1
    register = 1
    signal = 0
    screen = '\n'
    for command in input:
        screen += '#' if register <= cycle % 40 <= register + 2 else '.'
        cycle += 1
        command = command.split(' ')
        if command[0] == 'addx':
            if cycle % 40 == 20:
                signal += cycle * register
            elif cycle % 40 == 1:
                screen += '\n'

            screen += '#' if register <= cycle % 40 <= register + 2 else '.'
            cycle += 1
            register += int(command[1])

        if cycle % 40 == 20:
            signal += cycle * register
        if cycle % 40 == 1:
            screen += '\n'
    return screen
