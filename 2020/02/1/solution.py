def check(s):
    (rule, password) = s.split(':')
    (amount, letter) = rule.split(' ')
    (lower, upper) = amount.split('-')
    count = password.count(letter)
    return count >= int(lower) and count <= int(upper)


def solve(in_file):
    with open(in_file) as f:
        passwords = f.readlines()
    return sum(1 for password in passwords if check(password))


print(solve('input.txt'))
