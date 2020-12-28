from collections import defaultdict
from itertools import combinations
from math import prod
'''
Part One - Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
Part Two - How many # are not part of a sea monster?
'''

MONSTER_PATTERN = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)


def parse_data(data):
    raw_tiles = []
    raw_tile = []
    for line in data:
        if line == '':
            raw_tiles.append(raw_tile)
            raw_tile = []
        else:
            raw_tile.append(line)

    tiles = dict()

    for tile in raw_tiles:
        tile_id = int(tile[0][5:-1])
        tiles[tile_id] = tile[1:]
    return tiles


def get_edge(tile, side):
    if side == 'u':
        return tile[0]
    if side == 'd':
        return tile[-1]

    line = ''
    if side == 'l':
        for row in tile:
            line += row[0]
    elif side == 'r':
        for row in tile:
            line += row[-1]
    return line


def find_correct_tiles(tiles):
    matching_sides = defaultdict(str)
    corners = {}

    for id_a, id_b in combinations(tiles, 2):
        tile_a, tile_b = tiles[id_a], tiles[id_b]

        for side_a in 'udlr':
            for side_b in 'udlr':
                edge_a, edge_b = get_edge(
                    tile_a, side_a), get_edge(tile_b, side_b)

                if edge_a == edge_b or edge_a == edge_b[::-1]:
                    matching_sides[id_a] += side_a
                    matching_sides[id_b] += side_b

    for tile_id, sides in matching_sides.items():
        if len(sides) == 2:
            corners[tile_id] = sides

    return corners


def rotate_90_clockwise(tile):
    new_tile = []
    for char in range(len(tile[0])):
        new_row = ''
        for row in tile[::-1]:
            new_row += row[char]
        new_tile.append(new_row)
    return new_tile


def orientations(tile):
    yield tile
    for _ in range(3):
        tile = rotate_90_clockwise(tile)
        yield tile


def arrangements(tile):
    yield from orientations(tile)
    yield from orientations(tile[::-1])


def matching_tile(tile, tiles, side_a, side_b):
    prev_side = get_edge(tile, side_a)

    # Iterate over all possible tiles
    for other_id, other in tiles.items():
        if tile is other:
            continue

        # Arrange second tile in any possible way
        for other in arrangements(other):
            # Until the two sides match
            if prev_side == get_edge(other, side_b):
                tiles.pop(other_id)
                return other


def matching_row(prev, tiles, tiles_per_row):
    yield prev
    for _ in range(tiles_per_row - 1):
        tile = matching_tile(prev, tiles, 'e', 'w')
        prev = tile
        yield prev


def strip_edges(matrix):
    return [row[1:-1] for row in matrix[1:-1]]


def build_image(top_left_tile, tiles, image_dimension):
    # Start from the top left
    first = top_left_tile
    image = []

    while 1:
        # Get a row of matching tiles
        image_row = matching_row(first, tiles, image_dimension)
        # Strip the outermost edges from each of them
        image_row = map(strip_edges, image_row)
        # Add together each row of the tiles into a single big row, and add it to the final image
        image.extend(map(''.join, zip(*image_row)))

        # Do this until tiles run out
        if not tiles:
            break

        # Match the first tile of the next row, which is south of the first tile of the current row
        first = matching_tile(first, tiles, 's', 'n')

    return image


def count_pattern(image, pattern):
    pattern_h, pattern_w = len(pattern), len(pattern[0])
    image_sz = len(image)

    deltas = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17),
              (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]

    for img in arrangements(image):
        n = 0
        for r in range(image_sz - pattern_h):
            for c in range(image_sz - pattern_w):
                if all(img[r + dr][c + dc] == '#' for dr, dc in deltas):
                    n += 1

        if n != 0:
            return n


def partOne(content):
    tiles = parse_data(content)
    corner_tiles = find_correct_tiles(tiles)
    return prod(corner_tiles)


def partTwo(content):
    tiles = parse_data(content)
    corner_tiles = find_correct_tiles(tiles)
    top_left_id, matching_sides = corner_tiles.popitem()
    top_left = tiles[top_left_id]
    image_dim = 12

    if matching_sides in ('ur', 'ru'):
        top_left = rotate_90_clockwise(top_left)
    elif matching_sides in ('ul', 'lu'):
        top_left = rotate_90_clockwise(rotate_90_clockwise(top_left))
    elif matching_sides in ('dl', 'ld'):
        top_left = rotate_90_clockwise(
            rotate_90_clockwise(rotate_90_clockwise(top_left)))

    tiles.pop(top_left_id)
    image = build_image(top_left, tiles, image_dim)
    monster_cells = sum(row.count('#') for row in MONSTER_PATTERN)
    water_cells = sum(row.count('#') for row in image)
    n_monsters = count_pattern(image, MONSTER_PATTERN)
    roughness = water_cells - n_monsters * monster_cells
    return roughness
