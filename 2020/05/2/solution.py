def divide(l, direction):
    if direction in ("F", "L"):
        return l[: (len(l) // 2)]
    elif direction in ("B", "R"):
        return l[(len(l) // 2) :]
    return None


def seat(code):
    row = range(128)
    i = 0
    while i < 7:
        row = divide(row, code[i])
        i += 1
    column = range(8)
    j = 0
    while j < 3:
        column = divide(column, code[7 + j])
        j += 1
    return (int(row[0]) * 8) + int(column[0])


def solve(in_file):
    with open(in_file) as f:
        codes = f.read().splitlines()
    ids = [seat(code) for code in codes]
    return (set(range(min(ids), max(ids))) - set(ids)).pop()


print(solve("input.txt"))

# print(seat('FBFBBFFRLR')) # want 357
# print(seat('BFFFBBFRRR')) # want 567
# print(seat('FFFBBBFRRR')) # want 119
# print(seat('BBFFBBFRLL')) # want 820
# print(divide(range(128), 'F'))
