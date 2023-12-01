from operator import itemgetter
''' 
Part One - Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?
Part Two - Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?
'''


def calc_sum(mixed_file):
    zero_first_index = list(map(itemgetter(1), mixed_file)).index(0)
    sum = 0
    for nth in [1000, 2000, 3000]:
        nth_index = (nth + zero_first_index) % len(mixed_file)
        sum += mixed_file[nth_index][1]
    return sum


def mixin(original, times=1):
    mixed_file = original[:]
    for _ in range(times):
        for (orig_i, value) in original[:]:  # Copy of the original file
            start_index = mixed_file.index((orig_i, value))
            mixed_file.pop(start_index)
            new_index = (start_index + value) % len(mixed_file)
            if new_index == 0 and value < 0:
                new_index = len(mixed_file)
            mixed_file.insert(new_index, (orig_i, value))
    return mixed_file


def part_one(input):
    original = [(i, int(n)) for i, n in enumerate(input)]
    mixed_file = mixin(original)
    sum = calc_sum(mixed_file)
    return sum


def part_two(input):
    DEC_KEY = 811589153
    MIXIN_TIMES = 10
    original = [(i, int(n) * DEC_KEY) for i, n in enumerate(input)]
    mixed_file = mixin(original, times=MIXIN_TIMES)
    sum = calc_sum(mixed_file)
    return sum
