def apply_mask(integer, mask):
    mask = list(reversed(list(mask)))
    for i in range(len(mask)):
        if mask[i] == '1':
            integer = integer | (1 << i)
        elif mask[i] == '0':
            integer = integer & ~(1 << i)
    return integer


# print(apply_mask(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')) # 73


def solve(in_file):
    with open(in_file) as f:
        instructions = f.readlines()
    mem = {}
    mask = "X" * 36
    for instruction in instructions:
        (command, value) = instruction.strip("\n").split("=")
        if command.strip() == "mask":
            mask = value.strip()
        else:
            address = command.strip().lstrip("mem[").rstrip("]")
            mem[address] = apply_mask(int(value), mask)
    return sum(mem.values())


# print(solve("sample.txt"))  # 165
print(solve("input.txt"))  # 6631883285184
