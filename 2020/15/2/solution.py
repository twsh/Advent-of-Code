INPUT = [0, 3, 1, 6, 7, 5]
SAMPLE = [0, 3, 6]


def solve(start):
    history = {}
    for v, k in enumerate(start[:-1]):
        history[k] = v + 1
    last = start[-1]
    turn = len(start) + 1
    while turn <= 30000000:
        if last not in history:
            say = 0
        else:
            say = (turn - 1) - history[last]
        history[last] = turn - 1
        last = say
        turn += 1
    return last


# print(solve(SAMPLE)) # 175594
print(solve(INPUT))  # 6007666
