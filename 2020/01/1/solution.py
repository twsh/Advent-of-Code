def solve(in_file):
    with open(in_file) as f:
        numbers = f.readlines()

    for m in numbers:
        for n in numbers:
            if int(m) + int(n) == 2020:
                return int(m) * int(n)


print(solve('input.txt'))
