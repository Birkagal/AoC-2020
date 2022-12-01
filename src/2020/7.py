''' 
Part One - How many bag colors can eventually contain at least one shiny gold bag?
Part Two - How many individual bags are required inside your single shiny gold bag?
'''


def part_one(content):
    bags_dict = put_bags_in_dict(content)
    keys_with_shiny_gold = check_for_bag(bags_dict, 'shiny gold')
    queue = []
    bags = []
    checked_bags = []
    for key in keys_with_shiny_gold:
        queue.append(key)
    while queue:
        bags = queue.copy()
        for bag in bags:
            if bag not in checked_bags:
                checked_bags.append(bag)
            new_bags = check_for_bag(bags_dict, bag)
            for bag_element in new_bags:
                if bag_element not in queue:
                    queue.append(bag_element)
            queue.pop(0)
    return len(checked_bags)


def check_for_bag(bags_dict, bag):
    bags = []
    for key in bags_dict:
        for bag_element in bags_dict[key]:
            if bag in bag_element:
                bags.append(key)
    return bags


def put_bags_in_dict(content):
    key_bag = ''
    bag = ''
    bags_dict = dict()
    for line in content:
        bags_contained = []
        line = line.split()
        key_bag = line[0] + ' ' + line[1]
        line = line[4:]
        bags_dict[key_bag] = []
        bag = ''
        for word in line:
            if word in 'no other':
                break
            if word in ['bags,', 'bags.', 'bag,', 'bag.']:
                bags_contained.append(bag.strip())
                bag = ''
            elif word.isdigit():
                continue
            else:
                bag += word + ' '
        bags_dict[key_bag] = bags_contained
    return bags_dict


def split(txt, seps):
    default_sep = seps[0]
    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]


def part_two(content):
    bags_dict = put_bags_in_dict_with_numbers(content)
    return go_inside_bag(bags_dict, 'shiny gold')


def put_bags_in_dict_with_numbers(content):
    key_bag = ''
    bag = ''
    bags_dict = dict()
    for line in content:
        bags_contained = []
        line = line.split()
        key_bag = line[0] + ' ' + line[1]
        line = line[4:]
        bags_dict[key_bag] = []
        bag = ''
        for word in line:
            if word in 'no other':
                bags_contained = [1]
                break
            if word in ['bags,', 'bags.', 'bag,', 'bag.']:
                bags_contained.append(bag.strip())
                bag = ''
            elif word.isdigit():
                bags_contained.append(int(word))
            else:
                bag += word + ' '
        bags_dict[key_bag] = bags_contained
    return bags_dict


def go_inside_bag(bags_dict, bag):
    if bags_dict[bag] == [1]:
        return 0
    total = 0
    multip = 1
    for bag in bags_dict[bag]:
        if isinstance(bag, int):
            multip = bag
            total += multip
        else:
            total += multip*go_inside_bag(bags_dict, bag)
    return total
