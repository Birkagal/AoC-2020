''' 
Part One - Find the two entries that sum to 2020; what do you get if you multiply them together?
Part Two - what is the product of the three entries that sum to 2020?
'''


def part_one(numbers):
    numbers = sorted([int(number) for number in numbers])
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (numbers[i]+numbers[j]) == 2020:
                return numbers[i]*numbers[j]


def part_two(numbers):
    numbers = sorted([int(number) for number in numbers])
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for q in range(j, len(numbers)):
                if (numbers[i]+numbers[j]+numbers[q]) == 2020:
                    return numbers[i]*numbers[j]*numbers[q]
