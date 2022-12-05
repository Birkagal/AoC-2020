''' 
Part One - Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
Part Two - Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''


ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part_one(input):
    priorities = []
    for line in input:
        len_half = len(line) // 2
        first_compartment = line[:len_half]
        second_compartment = line[len_half:]

        shared_item = ''.join({
            char for char in first_compartment
            if char in second_compartment
        })
        priorities.append(
            ALPHABET.index(shared_item) + 1
        )

    return sum(priorities)


def part_two(input):
    priorities = []
    for l1, l2, l3 in zip(*[iter(input)]*3):  # Get 3 lines at once
        shared_item = ''.join({
            char for char in l1
            if char in l2 and char in l3
        })
        priorities.append(
            ALPHABET.index(shared_item) + 1
        )

    return sum(priorities)
