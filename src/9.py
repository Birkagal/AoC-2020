''' 
Part One - find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it.
Part Two - What is the encryption weakness in your XMAS-encrypted list of numbers?
'''


def find_invalid_number(data, preamble_length):
    preambles = []
    found_number = 0
    found_match = False
    for preamble in range(preamble_length):
        preambles.append(int(data[preamble]))
    data = data[preamble_length:]
    for number in data:
        number = int(number)
        copy_preambles = preambles.copy()
        for preamble in preambles:
            stil_left = number - preamble
            copy_preambles.remove(preamble)
            if stil_left in copy_preambles:
                found_match = True
                break
            copy_preambles.append(preamble)
        if found_match:
            found_match = False
        else:
            return number
        preambles.pop(0)
        preambles.append(number)
    return -1


def partOne(content):
    return find_invalid_number(content, 25)


def partTwo(content):
    invalid_number = find_invalid_number(content, 25)
    sum_lst = []
    total_goal = invalid_number
    found_match = False
    for index in range(len(content)):
        while total_goal > 0:
            number = int(content[index])
            total_goal -= number
            sum_lst.append(number)
            if total_goal == 0:
                found_match = True
                break
            index += 1
        if found_match:
            break
        total_goal = invalid_number
        sum_lst = []
    sum_lst.sort()
    return sum_lst[0]+sum_lst[-1]
