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


def solve(in_file):
    (points, width, height) = parse_map(in_file)
    trees = 0
    x = 0
    y = 0
    while y < height:
        if points[(x, y)] == "#":
            trees += 1
        x = (x + 3) % width
        y += 1
    return trees


# print(solve('sample.txt'))
print(solve("input.txt"))
