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


def look(seat, grid, direction):
    (x, y) = seat
    if direction == "right":
        w = x + 1
        z = y
    elif direction == "left":
        w = x - 1
        z = y
    elif direction == "down":
        w = x
        z = y + 1
    elif direction == "up":
        w = x
        z = y - 1
    elif direction == "upright":
        w = x + 1
        z = y - 1
    elif direction == "upleft":
        w = x - 1
        z = y - 1
    elif direction == "downright":
        w = x + 1
        z = y + 1
    elif direction == "downleft":
        w = x - 1
        z = y + 1
    try:
        if grid[(w, z)] in ("#", "L"):
            return grid[(w, z)]
        else:
            return look((w, z), grid, direction)
    except KeyError:
        return None


def check_seat(seat, grid):
    visible = 0
    directions = [
        "up",
        "down",
        "left",
        "right",
        "upleft",
        "downleft",
        "upright",
        "downright",
    ]
    for direction in directions:
        seen = look(seat, grid, direction)
        if seen == "#":
            visible += 1
    return visible


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
            elif grid[seat] == "#" and check_seat(seat, grid) >= 5:
                updates[seat] = "L"
        if updates:
            for update in updates:
                grid[update] = updates[update]
            updates = {}
        else:
            unstable = False
    return count_occupied(grid)


# print(solve("sample.txt"))  # 26
print(solve("input.txt"))  # 2045
