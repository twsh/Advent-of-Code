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


def solve(in_file):
    with open(in_file) as f:
        numbers = get_numbers(f.readlines())
    return find_weakness(25, numbers)


# print(solve('sample.txt')) # 127
print(solve("input.txt"))  # 248131121
