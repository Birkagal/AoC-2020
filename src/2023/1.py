import re

''' 
Part One - Consider your entire calibration document. What is the sum of all of the calibration values?
Part Two - what is the product of the three entries that sum to 2020?
'''


def check_digit(string) -> int | None:
    DIGIT_WORDS = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    if str.isdigit(string[0]):
        return int(string[0])

    for d in DIGIT_WORDS:
        if string.startswith(d):
            return DIGIT_WORDS[d]

    return 0


def part_one(input: list[str]):
    sum = 0
    for line in input:
        nums = list(map(int, re.findall(r'\d', line)))
        if len(nums) == 0:
            continue
        sum += nums[0] * 10 + nums[-1]

    return sum


def part_two(input: list[str]):
    sum = 0
    for line in input:
        for idx in range(len(line)):
            digit1 = check_digit(line[idx:])
            if digit1:
                break

        for idx in range(len(line) - 1, -1, -1):
            digit2 = check_digit(line[idx:])
            if digit2:
                break
        sum += digit1 * 10 + digit2

    return sum
