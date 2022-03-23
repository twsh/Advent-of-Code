import re


def check_bags(rule, start, target):
    to_check = []
    to_check += list(rule[start])
    while to_check:
        current = to_check.pop()
        if current == target:
            return True
        else:
            to_check += list(rule[current])
    return False


def get_bag(s):
    s = re.sub("[0-9]", "", s)
    s = re.sub("bags", "", s)
    s = re.sub("bag", "", s)
    s = re.sub("no other", "", s)
    s = s.rstrip("\.\n")
    s = s.strip()
    return s


def make_rules(in_file):
    rule = {}
    lines = in_file.readlines()
    for line in lines:
        (bag, contents) = line.split("contain")
        bag = get_bag(bag)
        contents = [get_bag(x) for x in contents.split(",")]
        rule[bag] = contents
        if rule[bag] == [""]:
            rule[bag] = []
    return rule


def solve(in_file):
    with open(in_file) as f:
        rule = make_rules(f)
    suitable_bags = [
        start for start in rule.keys() if check_bags(rule, start, "shiny gold")
    ]
    return len(suitable_bags)


# print(solve('sample.txt')) # 4
print(solve("input.txt"))  # 112
