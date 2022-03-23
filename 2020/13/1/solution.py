def get_next(bus, time):
    if bus == "x":
        return None
    else:
        next_time = 0
        while next_time < time:
            next_time += int(bus)
        return next_time


# print(get_next(59, 939))


def solve(in_file):
    with open(in_file) as f:
        (time, buses) = f.readlines()
    time = int(time.strip("\n"))
    buses = buses.strip("\n").split(",")
    buses = [int(bus) for bus in buses if bus != "x"]
    next_buses = sorted(
        [(bus, get_next(bus, time)) for bus in buses], key=lambda x: x[1]
    )
    (next_bus, departure) = next_buses[0]
    return next_bus * (departure - time)


# print(solve('sample.txt')) # 295
print(solve("input.txt"))  # 156
