import math


def parse_map(in_file):
    with open(in_file) as f:
        lines = f.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    points = {}
    for x in range(width):
        for y in range(height):
            points[(x, y)] = lines[y][x]
    return points, width, height


def check_slope(points, width, height, right, down):
    trees = 0
    x = 0
    y = 0
    while y < height:
        if points[(x, y)] == "#":
            trees += 1
        x = (x + right) % width
        y += down
    return trees


def solve(in_file, slopes):
    (points, width, height) = parse_map(in_file)
    trees = []
    for slope in slopes:
        (right, down) = slope
        trees.append(check_slope(points, width, height, right, down))
    return math.prod(trees)


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# print(solve('sample.txt'))
print(solve("input.txt", slopes))
