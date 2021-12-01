from util.io import get_lines, get_input


def part1():
    previous = -1
    count = 0

    for depth in get_lines(1, int):
        if depth > previous > 0:
            count += 1

        previous = depth

    return count


def part2():
    prev = -1
    prev2 = -1
    prev3 = -1
    count = 0

    for depth in get_lines(1, int):
        prev_window = prev3 + prev2 + prev
        current_window = prev2 + prev + depth

        if current_window > prev_window and prev3 > 0:
            count += 1

        prev3 = prev2
        prev2 = prev
        prev = depth

    return count


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
