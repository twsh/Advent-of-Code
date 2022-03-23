def run(instructions):
    accumulator = 0
    pointer = 0
    visited = []
    while pointer < len(instructions):
        if pointer in visited:
            print("I am looping!")
            raise Exception
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


replace = {"nop": "jmp", "jmp": "nop"}


def debug(instructions):
    pointer = 0
    while pointer < len(instructions):
        (instruction, value) = instructions[pointer].split(" ")
        if instruction in ("nop", "jmp"):
            new_instruction = replace[instruction] + " " + value
            new_instructions = (
                instructions[:pointer] + [new_instruction] + instructions[pointer + 1 :]
            )
            try:
                accumulator = run(new_instructions)
                print("These new instructions worked!")
                print(*new_instructions)
                return accumulator
            except Exception:
                print("These new instructions didn't work!")
        pointer += 1


def solve(in_file):
    with open(in_file) as f:
        instructions = f.read().strip("\n").split("\n")
    return debug(instructions)


# print(solve("sample.txt"))  # 8
print(solve("input.txt"))  # 1688
