from util.io import get_lines


def part1():
    h = 0
    d = 0

    for line in get_lines(2):
        parts = line.split(' ')
        cmd = parts[0]
        amount = int(parts[1])

        if cmd == 'forward':
            h += amount
        elif cmd == 'down':
            d += amount
        elif cmd == 'up':
            d -= amount

    return h * d


def part2():
    h = 0
    d = 0
    a = 0

    for line in get_lines(2):
        parts = line.split(' ')
        cmd = parts[0]
        amount = int(parts[1])

        if cmd == 'forward':
            h += amount
            d += a * amount
        elif cmd == 'down':
            a += amount
        elif cmd == 'up':
            a -= amount

    return h * d


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
