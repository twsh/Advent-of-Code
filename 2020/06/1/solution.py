def count(s):
    return len(set(s.replace("\n", "")))


def solve(in_file):
    with open(in_file) as f:
        answers = f.read().split("\n\n")
    return sum([count(answer) for answer in answers])


# print(count('abc')) # 3
# print(count('a\nb\nc')) # 3
# print(count('ab\nac')) # 3
# print(count('a\na\na\na')) # 1
# print(count('b')) # 1
# print(solve('sample.txt'))
print(solve("input.txt"))
