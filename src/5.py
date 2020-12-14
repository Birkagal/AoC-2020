import math
''' 
Part One - What is the highest seat ID on a boarding pass?
Part Two - What is the ID of your seat?
'''


def partOne(content):
    ids = calculate_ids(content)
    return max(ids)


def partTwo(content):
    ids = calculate_ids(content)
    return [x for x in range(ids[0], ids[-1]+1) if x not in ids][0]


# get list of boarding passes, calculate row and seat and save multiplication in ids. return ids.
def calculate_ids(content):
    row = 0
    ids = []
    for ticket in content:
        counter = 0
        start = 0
        finish = 127
        for letter in ticket:
            counter += 1
            if letter in ['F', 'L']:
                finish = (finish+start) // 2
            elif letter in ['B', 'R']:
                start = math.ceil((finish+start) / 2)
            if counter == 7:
                row = start
                start = 0
                finish = 7
            elif counter == len(ticket):
                ids.append(row*8+start)

    ids.sort()
    return ids
