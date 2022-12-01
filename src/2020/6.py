''' 
Part One - For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
Part Two - For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''


def part_one(content):
    answers = []
    group_answer = set()
    groups = split_text(content)
    for group in groups:
        for person in group:
            for answer in person:
                group_answer.add(answer)
        answers.append(len(group_answer))
        group_answer = set()
    return sum(answers)


def part_two(content):
    groups = split_text(content)
    first_person_answer = []
    group_answer = []
    is_first = True
    answers = []
    for group in groups:
        for person in group:
            if is_first:
                group_answer = list(person)
                is_first = False
            else:
                first_person_answer = group_answer.copy()
                for answer in first_person_answer:
                    if answer not in person:
                        group_answer.remove(answer)
        answers.append(len(group_answer))
        is_first = True
    return sum(answers)


def split_text(text):
    groups = []
    group = []
    for line in text:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    if group:
        groups.append(group)
    return groups
