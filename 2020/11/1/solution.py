def parse_map(in_file):
    with open(in_file) as f:
        lines = f.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    points = {}
    for x in range(width):
        for y in range(height):
            points[(x, y)] = lines[y][x]
    return points


def check_seat(seat, grid):
    adjacent = 0
    (x, y) = seat
    coordinates = [(a, b) for a in [x - 1, x, x + 1] for b in [y - 1, y, y + 1]]
    for coordinate in coordinates:
        try:
            if grid[coordinate] == "#":
                adjacent += 1
        except KeyError:
            pass
    return adjacent


def count_occupied(grid):
    total = 0
    for seat in grid:
        if grid[seat] == "#":
            total += 1
    return total


def solve(in_file):
    grid = parse_map(in_file)
    unstable = True
    updates = {}
    while unstable:
        for seat in grid:
            if grid[seat] == "L" and check_seat(seat, grid) == 0:
                updates[seat] = "#"
            elif grid[seat] == "#" and check_seat(seat, grid) > 4:
                updates[seat] = "L"
        if updates:
            for update in updates:
                grid[update] = updates[update]
            updates = {}
        else:
            unstable = False
    return count_occupied(grid)


# print(solve('sample.txt')) # 37
print(solve("input.txt"))  # 2265
