''' 
Part One - The Elves are starting to get cold. What SNAFU number do you supply to Bob's console?
Part Two - DONE ;)
'''


def toSNAFU(n):
    snafu = ''

    while n:
        n, digit = divmod(n, 5)

        if digit > 2:
            n += 1

            if digit == 3:
                snafu += '='
            else:
                snafu += '-'
        else:
            snafu += str(digit)

    return snafu[::-1]


def fromSNAFU(snafu):
    snafu = snafu[::-1]  # reverse the string
    decimal = 0
    for i, digit in enumerate(snafu):
        if digit == '-':
            digit = '-1'
        elif digit == '=':
            digit = '-2'
        decimal += int(digit) * (5 ** i)
    return decimal


def part_one(input):
    amount = sum([fromSNAFU(value) for value in input])
    return toSNAFU(amount)


def part_two(input):
    return 'FINISHED!'
