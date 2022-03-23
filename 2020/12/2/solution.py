def move(position, direction, distance):
    if direction == "N":
        return add_vector(position, (0, distance))
    elif direction == "S":
        return add_vector(position, (0, -distance))
    elif direction == "E":
        return add_vector(position, (distance, 0))
    elif direction == "W":
        return add_vector(position, (-distance, 0))


def add_vector(position, waypoint):
    (x1, y1) = position
    (x2, y2) = waypoint
    return (x1 + x2, y1 + y2)


# https://en.wikipedia.org/wiki/Rotation_matrix#Common_rotations
rotation_to_matrix = {
    90: ((0, -1), (1, 0)),
    180: ((-1, 0), (0, -1)),
    270: ((0, 1), (-1, 0)),
}


def multiply_matrix(waypoint, rotation):
    (a, b) = rotation
    (a1, a2) = a
    (b1, b2) = b
    (x, y) = waypoint
    return (
        (a1 * x) + (a2 * y),
        (b1 * x) + (b2 * y),
    )


def solve(in_file):
    with open(in_file) as f:
        instructions = f.readlines()
    position = (0, 0)
    waypoint = (10, 1)
    for instruction in instructions:
        code = instruction[0]
        value = int(instruction[1:].rstrip("\n"))
        if code == "R":
            waypoint = multiply_matrix(waypoint, rotation_to_matrix[360 - value])
        elif code == "L":
            waypoint = multiply_matrix(waypoint, rotation_to_matrix[value])
        elif code == "F":
            while value:
                position = add_vector(position, waypoint)
                value -= 1
        elif code in ("N", "S", "E", "W"):
            waypoint = move(waypoint, code, value)
    (y, x) = position
    manhattan = abs(x) + abs(y)
    return manhattan


# print(solve('sample.txt')) # 286
print(solve("input.txt"))  # 156735
