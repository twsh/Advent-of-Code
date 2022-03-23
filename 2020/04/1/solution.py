def parse_passport(s):
    passport = {}
    data = s.replace("\n", " ").split(" ")
    for field in data:
        if field:
            (k, v) = field.strip().split(":")
            passport[k] = v
    return passport


def check_passport(d):
    return (
        "byr" in d
        and "iyr" in d
        and "eyr" in d
        and "hgt" in d
        and "hcl" in d
        and "ecl" in d
        and "pid" in d
    )


def solve(in_file):
    with open(in_file) as f:
        batch = f.read()

    parsed = [parse_passport(record) for record in batch.split("\n\n")]

    return sum(1 for passport in parsed if check_passport(passport))


print(solve("input.txt"))
