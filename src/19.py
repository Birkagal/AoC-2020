import re
'''
Part One - How many messages completely match rule 0?
Part Two - After updating rules 8 and 11, how many messages completely match rule 0?
'''


def parse_input(input):
    rules = {}

    for line in input:
        if not line:
            break

        rule_id, options = line.split(': ')
        rule_id = int(rule_id)

        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split('|'):
                rule.append(tuple(map(int, option.split())))

        rules[rule_id] = rule

    return rules


def build_regexp(rules, rule=0):
    rule = rules[rule]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        option_str = ''
        for sub_rule in option:
            option_str += build_regexp(rules, sub_rule)
        options.append(option_str)

    return '(' + '|'.join(options) + ')'


def build_regexp_recursive(rules, rule=0):
    if rule == 8:
        return '(' + build_regexp_recursive(rules, 42) + ')+'

    if rule == 11:
        a = build_regexp_recursive(rules, 42)
        b = build_regexp_recursive(rules, 31)

        options = []
        for n in range(1, 40):
            options.append('{a}{{{n}}}{b}{{{n}}}'.format(a=a, b=b, n=n))

        return '(' + '|'.join(options) + ')'

    rule = rules[rule]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        option = ''.join(build_regexp_recursive(rules, r) for r in option)
        options.append(option)

    return '(' + '|'.join(options) + ')'


def partOne(content):
    rules = parse_input(content)
    regex = build_regexp(rules)
    rexp = re.compile('^' + regex + '$')
    valid = 0
    start_checking = False
    for msg in content:
        if start_checking:
            if rexp.match(msg):
                valid += 1
        else:
            if msg == '':
                start_checking = True
    return valid


def partTwo(content):
    rules = parse_input(content)
    regex = build_regexp_recursive(rules)
    rexp = re.compile('^' + regex + '$')
    valid = 0
    start_checking = False
    for msg in content:
        if start_checking:
            if rexp.match(msg):
                valid += 1
        else:
            if msg == '':
                start_checking = True
    return valid
