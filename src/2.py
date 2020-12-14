''' 
Part One - How many passwords are valid according to their policies?
Part Two - How many passwords are valid according to the new interpretation of the policies?
'''


def partOne(content):
    regex = "-+:"
    low, high = 0, 0
    digit = ''
    total_passwords, counter = 0, 0
    for line in content:
        line = line.split(regex)[0].split()
        low, high = int(line[0].split("-")[0]), int(line[0].split("-")[1])
        digit = line[1][0]
        counter = 0
        for char in line[2]:
            if char == digit:
                counter = counter + 1
        if low <= counter <= high:
            total_passwords = total_passwords + 1
    return total_passwords


def partTwo(content):
    regex = "-+:"
    first, second = 0, 0
    digit = ''
    total_passwords = 0
    for line in content:
        line = line.split(regex)[0].split()
        first, second = int(line[0].split("-")[0]), int(line[0].split("-")[1])
        char = line[1][0]
        if (line[2][first-1] == char) ^ (line[2][second-1] == char):
            total_passwords = total_passwords + 1
    return total_passwords
