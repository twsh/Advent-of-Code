def apply_mask(integer, mask):
    mask = list(reversed(list(mask)))
    for i in range(len(mask)):
        if mask[i] == "1":
            integer = integer | (1 << i)
    return integer


def get_addresses(address, mask):
    addresses = [apply_mask(address, mask)]
    mask = list(reversed(list(mask)))
    for i in range(len(mask)):
        if mask[i] == "X":
            new_addresses = []
            for x in addresses:
                new_addresses.append(x | (1 << i))
                new_addresses.append(x & ~(1 << i))
            addresses = new_addresses
    return addresses


# print(get_addresses(42, '000000000000000000000000000000X1001X'))


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
            address = int(command.strip().lstrip("mem[").rstrip("]"))
            addresses = get_addresses(address, mask)
            for i in addresses:
                mem[i] = int(value.strip())
    return sum(mem.values())


# print(solve("sample2.txt"))  # 208
print(solve("input.txt"))  # 3161838538691
