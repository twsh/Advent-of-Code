def solve(in_file):
    with open(in_file) as f:
        numbers = f.readlines()

    for m in numbers:
        for n in numbers:
            for o in numbers:
                if int(m) + int(m) + int(o) == 2020:
                    return int(m) * int(n) * int(o)


print(solve('input.txt'))
