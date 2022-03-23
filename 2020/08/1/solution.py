def check(instructions):
    accumulator = 0
    pointer = 0
    visited = []
    while pointer not in visited:
        visited.append(pointer)
        (instruction, value) = instructions[pointer].split(" ")
        if instruction == "nop":
            pointer += 1
        elif instruction == "acc":
            pointer += 1
            accumulator += int(value)
        elif instruction == "jmp":
            pointer += int(value)
    return accumulator


def solve(in_file):
    with open(in_file) as f:
        instructions = f.readlines()
    return check(instructions)


print(solve("sample.txt"))  # 5
print(solve("input.txt"))  # 1930
