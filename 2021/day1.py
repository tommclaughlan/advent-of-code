from util.io import get_lines


def part1():
    previous = -1
    count = 0

    for depth in get_lines('day1', int):
        if previous < 0:
            previous = depth
            continue

        if depth > previous:
            count += 1

        previous = depth

    return count


def part2():
    prev = -1
    prev2 = -1
    prev3 = -1
    count = 0

    for depth in get_lines('day1', int):
        if prev3 < 0:
            prev3 = prev2
            prev2 = prev
            prev = depth
            continue

        prev_window = prev3 + prev2 + prev
        current_window = prev2 + prev + depth

        if current_window > prev_window:
            count += 1

        prev3 = prev2
        prev2 = prev
        prev = depth

    return count


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
