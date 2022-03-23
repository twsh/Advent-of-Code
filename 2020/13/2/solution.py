def solve(in_file):
    with open(in_file) as f:
        (time, buses) = f.readlines()
    buses = [x if x == "x" else int(x) for x in buses.split(",")]
    departures = sorted(
        filter(lambda x: x[1] != "x", enumerate(buses)),
        key=lambda x: x[1],
        reverse=True,
    )
    (first_offset, first_bus) = departures[0]
    first_departure = -first_offset % first_bus
    val = first_departure
    step = first_bus
    for departure in departures[1:]:
        (offset, bus) = departure
        while val % bus != -offset % bus:
            val += step
        step *= bus
    return val


# print(solve('sample.txt')) # 1068788
print(solve("input.txt"))  # 404517869995362
