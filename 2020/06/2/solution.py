def count(s):
    people = [set(person) for person in s.split("\n") if person]
    return len(set.intersection(*people))


def solve(in_file):
    with open(in_file) as f:
        answers = f.read().split("\n\n")
    return sum([count(answer) for answer in answers])


# print(count('abc')) # 3
# print(count('a\nb\nc')) # 0
# print(count('ab\nac')) # 1
# print(count('a\na\na\na')) # 1
# print(count('b')) # 1
# print(solve('sample.txt')) # 6
print(solve("input.txt"))
