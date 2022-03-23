import re


def count_bags(rule, bag):
    to_check = rule[bag]
    checked = []
    while any(to_check):
        current = to_check.pop()
        try:
            to_check += rule[current]
            checked += [current]
        except KeyError:
            pass
    return len(checked)


def get_bag(s):
    if not re.match("no other bags", s.strip()):
        number = int(s.strip()[0])
    else:
        number = 0
    s = re.sub("[0-9]", "", s)
    s = re.sub("bags", "", s)
    s = re.sub("bag", "", s)
    s = re.sub("no other", "", s)
    s = s.rstrip("\.\n")
    s = s.strip()
    return [s] * number


def make_rules(in_file):
    rule = {}
    lines = in_file.readlines()
    for line in lines:
        (bag, contents) = line.split("contain")
        bag = re.sub("bags", "", bag).strip()
        bags = []
        for x in contents.split(","):
            bags += get_bag(x)
        if not bags:
            rule[bag] = [""]
        else:
            rule[bag] = bags
    return rule


def solve(in_file):
    with open(in_file) as f:
        rule = make_rules(f)
    return count_bags(rule, "shiny gold")


print(solve("sample.txt"))  # 32
print(solve("input.txt"))  # 6260
