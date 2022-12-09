'''
Part One - Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
Part Two - Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
'''


DIRECTION_MAP = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def move_tail(head_coords, tail_coords):
    hx, hy = head_coords
    tx, ty = tail_coords
    dx, dy = hx - tx, hy - ty
    abs_dx = abs(dx)
    abs_dy = abs(dy)

    if abs_dx > 1 or abs_dy > 1:
        tx += dx if dx == 0 else dx // abs_dx
        ty += dy if dy == 0 else dy // abs_dy
    return tx, ty


def part_one(input):
    head_coords = (0, 0)
    tail_coords = (0, 0)
    unique_tail_positions = {tail_coords}
    for action in input:
        direction, steps = action.split(' ')
        for _ in range(int(steps)):
            dx, dy = DIRECTION_MAP[direction]
            head_coords = head_coords[0] + dx, head_coords[1] + dy
            tail_coords = move_tail(head_coords, tail_coords)
            unique_tail_positions.add(tail_coords)
    return len(unique_tail_positions)


def part_two(input):
    num_of_knots = 10
    knots = [(0, 0)] * num_of_knots
    unique_tail_positions = {knots[-1]}
    for action in input:
        direction, steps = action.split(' ')
        for _ in range(int(steps)):
            hx, hy = knots[0]
            dx, dy = DIRECTION_MAP[direction]
            knots[0] = (hx + dx, hy + dy)
            for i in range(num_of_knots - 1):
                knots[i + 1] = move_tail(knots[i], knots[i + 1])
                if knots[i + 1] == knots[i]:
                    break
            unique_tail_positions.add(knots[-1])
    return len(unique_tail_positions)
