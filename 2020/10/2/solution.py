def group_me(l):
    """
    https://stackoverflow.com/a/59378884/1926514
    """
    l.sort()
    sublist = []

    while l:
        v = l.pop(0)

        if not sublist or sublist[-1] in [v, v - 1]:
            sublist.append(v)
        else:
            yield sublist
            sublist = [v]

    if sublist:
        yield sublist


def extend(start, end, allowed):
    global count
    if abs(start - end) <= 3:
        count += 1
    else:
        for i in range(1, 4):
            if start + i in allowed:
                extend(start + i, end, allowed)


def count_ways(sequence):
    global count
    count = 0
    extend(min(sequence), max(sequence) + 3, sequence)
    return count


def solve(in_file):
    with open(in_file) as f:
        adapters = [int(x.strip("\n")) for x in f.readlines()]
    adapters = [0] + adapters + [max(adapters) + 3]
    sub_sequences = group_me(adapters)
    total = 1
    for sequence in sub_sequences:
        total = total * count_ways(sequence)
    return total


# print(solve('sample.txt')) # 8
# print(solve('sample2.txt')) # 19208
print(solve("input.txt"))  # 1322306994176
