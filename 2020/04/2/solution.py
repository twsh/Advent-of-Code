import re


def parse_passport(s):
    passport = {}
    for field in s.split():
        (k, v) = field.split(":")
        passport[k] = v
    return passport


def check_byr(s):
    return int(s) >= 1920 and int(s) <= 2002


def check_iyr(s):
    return int(s) >= 2010 and int(s) <= 2020


def check_eyr(s):
    return int(s) >= 2020 and int(s) <= 2030


def check_hgt(s):
    if s[-2:] == "cm":
        return int(s[:-2]) >= 150 and int(s[:-2]) <= 193
    elif s[-2:] == "in":
        return int(s[:-2]) >= 59 and int(s[:-2]) <= 76
    else:
        return False


def check_hcl(s):
    return re.match("#[0-9a-f]{6}", s) and len(s) == 7


def check_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(s):
    return re.match("[0-9]{9}", s) and len(s) == 9


def check_passport(d):
    try:
        return (
            check_byr(d["byr"])
            and check_iyr(d["iyr"])
            and check_eyr(d["eyr"])
            and check_hgt(d["hgt"])
            and check_hcl(d["hcl"])
            and check_ecl(d["ecl"])
            and check_pid(d["pid"]))
    except KeyError:
        return False


def solve(in_file):
    with open(in_file) as f:
        batch = f.read()
    parsed = [parse_passport(record) for record in batch.split("\n\n")]

    return sum(1 for passport in parsed if check_passport(passport))


# print(check_byr('2002')) # byr valid:   2002
# print(check_byr('2003')) # byr invalid: 2003

# print(check_hgt('60in')) # hgt valid:   60in
# print(check_hgt('190cm')) # hgt valid:   190cm
# print(check_hgt('190in')) # hgt invalid: 190in
# print(check_hgt('190')) #  hgt invalid: 190

# print(check_hcl('#123abc')) # hcl valid:   #123abc
# print(check_hcl('#123abz')) # hcl invalid: #123abz
# print(check_hcl('123abc')) # hcl invalid: 123abc

# print(check_ecl('brn')) # ecl valid:   brn
# print(check_ecl('wat')) # ecl invalid: wat

# print(check_pid('000000001')) # pid valid:   000000001
# print(check_pid('0123456789')) # pid invalid: 0123456789


# print(check_pid('087499704')) # pid:087499704
# print(check_hgt('74in')) # hgt:74in
# print(check_ecl('grn')) # ecl:grn
# print(check_iyr('2012')) # iyr:2012
# print(check_eyr('2030')) # eyr:2030
# print(check_byr('1980')) # byr:1980
# print(check_hcl('#623a2f')) # hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719


# print(solve('invalid.txt')) # want 0
# print(solve('valid.txt')) # want 4
print(solve("input.txt"))
