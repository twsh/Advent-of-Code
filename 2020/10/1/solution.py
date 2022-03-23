def get_differences(adapters):
    comparator = 0
    ones = 0
    threes = 0
    while adapters:
        if adapters[-1] - comparator == 3:
            threes += 1
        elif adapters[-1] - comparator == 1:
            ones += 1
        comparator = adapters.pop()
    return ones, threes


def solve(in_file):
    with open(in_file) as f:
        adapters = sorted([int(x.strip("\n")) for x in f.readlines()], reverse=True)
    (ones, threes) = get_differences(adapters)
    return ones * (threes + 1)


# print(solve('sample.txt')) # 35
print(solve('input.txt')) # 2048
