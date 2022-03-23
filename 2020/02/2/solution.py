def make_index(s):
    return int(s) - 1


def check(s):
    (rule, password) = s.split(":")
    (positions, letter) = rule.split(" ")
    (first, second) = positions.split("-")
    password = password.strip()
    return (password[make_index(first)] == letter) ^ (
        password[make_index(second)] == letter
    )


def solve(in_file):
    with open(in_file) as f:
        passwords = f.readlines()
    return sum(1 for password in passwords if check(password))


print(solve("input.txt"))
