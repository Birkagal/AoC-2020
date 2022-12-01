'''
Part One - Evaluate the expression on each line of the homework; what is the sum of the resulting values?
Part Two - What do you get if you add up the results of evaluating the homework problems using these new rules?
'''


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def peek(stack):
    return stack[-1] if stack else None


def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))


def greater_precedence(mode, op1, op2):
    if mode == 1:
        return True
    elif mode == 2:
        precedences = {'+': 1, '*': 0}
        return precedences[op1] >= precedences[op2]


def evaluate(mode, expression):
    values = []
    operators = []
    for token in expression:
        if token != ' ':
            if is_number(token):
                values.append(int(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                top = peek(operators)
                while top is not None and top != '(':
                    apply_operator(operators, values)
                    top = peek(operators)
                operators.pop()  # Discard the '('
            else:
                # Operator
                top = peek(operators)
                while top is not None and top not in "()" and greater_precedence(mode, top, token):
                    apply_operator(operators, values)
                    top = peek(operators)
                operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)

    return values[0]


def part_one(content):
    return sum([evaluate(1, expression) for expression in content])


def part_two(content):
    return sum([evaluate(2, expression) for expression in content])
