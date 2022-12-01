''' 
Part One - Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
Part Two - what is the product of the three entries that sum to 2020?
'''


def get_sorted_cal_sum(input):
    elfs_cal_sum = []
    index = 0
    for line in input:
        if line == '':
            index += 1
        else:
            try:
                elfs_cal_sum[index] += int(line)
            except:
                elfs_cal_sum.append(int(line))
    elfs_cal_sum.sort()
    return elfs_cal_sum


def part_one(input):
    sorted_cal_sum = get_sorted_cal_sum(input)
    return sorted_cal_sum[-1]


def part_two(input):
    sorted_cal_sum = get_sorted_cal_sum(input)
    return sum(sorted_cal_sum[-3:])
