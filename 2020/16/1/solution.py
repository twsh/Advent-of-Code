def parse(in_file):
    with open(in_file) as f:
        (notes, my_ticket, nearby_tickets) = f.read().split("\n\n")
    my_ticket = [int(n) for n in my_ticket.split("\n")[1].split(",")]
    new_notes = {}
    for note in notes.split("\n"):
        (k, v) = note.split(":")
        v = v.split("or")
        (a, b) = v
        new_notes[k] = ([int(n) for n in a.split("-")], [int(n) for n in b.split("-")])
    nearby_tickets = [
        [int(n) for n in ticket.split(",")]
        for ticket in nearby_tickets.split("\n")[1:-1]
    ]
    return new_notes, my_ticket, nearby_tickets


def check_number(number, notes):
    for field in notes:
        (first, second) = notes[field]
        (a, b) = first
        (c, d) = second
        if number in range(a, b + 1) or number in range(c, d + 1):
            return True
    return False


def solve(in_file):
    notes, my_ticket, nearby_tickets = parse(in_file)
    error = 0
    for ticket in nearby_tickets:
        for number in ticket:
            if not check_number(number, notes):
                error += number
    return error


# print(solve('sample.txt')) # 71
print(solve("input.txt"))  # 28882
