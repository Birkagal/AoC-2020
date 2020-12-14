''' 
Part One - Immediately before any instruction is executed a second time, what value is in the accumulator?
Part Two - What is the value of the accumulator after the program terminates?
'''


def run_the_program(instructions):
    acc = 0
    current_instruction = 0
    last_instruction = len(instructions)
    instruction_seen = []
    while True:
        if current_instruction in instruction_seen:
            return acc, False
        if current_instruction == last_instruction:
            return acc, True
        instruction = instructions[current_instruction].split()
        instruction_seen.append(current_instruction)
        if instruction[0] == 'nop':
            current_instruction += 1
        elif instruction[0] == 'acc':
            acc += int(instruction[1])
            current_instruction += 1
        elif instruction[0] == 'jmp':
            current_instruction += int(instruction[1])


def partOne(content):
    return run_the_program(content)[0]


def partTwo(content):
    instrucions = content
    current_line = 0
    finished = False
    for line in content:
        instrucions = content.copy()
        instruction = line.split()
        if instruction[0] == 'nop':
            instruction[0] = 'jmp'
            instrucions[current_line] = ' '.join(instruction)
            acc, finished = run_the_program(instrucions)
        elif instruction[0] == 'jmp':
            instruction[0] = 'nop'
            instrucions[current_line] = ' '.join(instruction)
            acc, finished = run_the_program(instrucions)
        if finished:
            return acc
        current_line += 1
