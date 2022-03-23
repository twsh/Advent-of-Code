def get_numbers(l):
    return [int(x.strip("\n")) for x in l]


def is_sum(candidates, number):
    for i in candidates:
        for j in candidates:
            if i + j == number and i != j:
                return True
    return False


def find_weakness(preamble, numbers):
    pointer = preamble
    while pointer < len(numbers):
        current = numbers[pointer]
        candidates = numbers[pointer - preamble : pointer]
        if not is_sum(candidates, current):
            return current
        pointer += 1
    return None


def find_range(numbers, weakness):
    subs = [
        numbers[i : i + j]
        for i in range(0, len(numbers))
        for j in range(1, len(numbers) - i + 1)
    ]
    for i in subs:
        if sum(i) == weakness:
            return i
    return None


def solve(in_file):
    with open(in_file) as f:
        numbers = get_numbers(f.readlines())
    weakness = find_weakness(25, numbers)
    sums = find_range(numbers, weakness)
    return min(sums) + max(sums)


# print(solve('sample.txt')) # 62
print(solve("input.txt"))  # 31580383
