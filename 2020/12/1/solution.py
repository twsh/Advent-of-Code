def move(position, direction, distance):
    (x, y) = position
    if direction == "N":
        return (x + distance, y)
    elif direction == "S":
        return (x - distance, y)
    elif direction == "E":
        return (x, y + distance)
    elif direction == "W":
        return (x, y - distance)


directions = {0: "N", 90: "E", 180: "S", 270: "W"}


def solve(in_file):
    with open(in_file) as f:
        instructions = f.readlines()
    position = (0, 0)
    heading = 90
    for instruction in instructions:
        code = instruction[0]
        value = int(instruction[1:].rstrip("\n"))
        if code == "R":
            heading = (heading + value) % 360
        elif code == "L":
            heading = (heading - value) % 360
        elif code == "F":
            position = move(position, directions[heading], value)
        elif code == "B":
            position = move(position, "E", -value)
        elif code in ("N", "S", "E", "W"):
            position = move(position, code, value)
    (x, y) = position
    manhattan = abs(x) + abs(y)
    return manhattan


# print(solve('sample.txt')) # 25
print(solve("input.txt"))  # 1032
