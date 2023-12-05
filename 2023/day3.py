from util.runner import Runner


def parse_number(map, x, y):
    start_x = x
    end_x = x

    while start_x > 0 and str(map[y][start_x - 1]).isdigit():
        start_x -= 1

    while end_x < len(map[y]) - 1 and str(map[y][end_x + 1]).isdigit():
        end_x += 1

    num = map[y][start_x:end_x + 1]

    return int(num)


class Day3(Runner):
    def part1(self):
        rows = [line for line in self.input]

        n_rows = len(rows)
        n_cols = len(rows[0])

        parts = []

        for y in range(0, n_rows):
            number = ""
            for x in range(0, n_cols):
                cell = str(rows[y][x])
                if cell.isdigit():
                    number += cell
                if (x == n_cols - 1 or not str(rows[y][x+1]).isdigit()) and number != "":
                    part_number = int(number)
                    y_range = []
                    if y > 0:
                        y_range.append(y - 1)
                    y_range.append(y)
                    if y < n_rows - 1:
                        y_range.append(y + 1)
                    x_range = []
                    if x > len(number):
                        x_range.append(x - len(number))
                    for i in range(0, len(number)):
                        x_range.append(x - len(number) + i + 1)
                    if x < n_cols - 1:
                        x_range.append(x + 1)

                    check_coords = []
                    for y_check in y_range:
                        for x_check in x_range:
                            if y_check != y:
                                check_coords.append([x_check, y_check])
                            elif x_check == x - len(number) or x_check > x:
                                check_coords.append([x_check, y_check])

                    is_part = False

                    for coord in check_coords:
                        check_cell = str(rows[coord[1]][coord[0]])
                        if not check_cell.isdigit() and check_cell != ".":
                            is_part = True

                    if is_part:
                        parts.append(part_number)

                    number = ""

        return sum(parts)

    def part2(self):
        rows = [line for line in self.input]

        n_rows = len(rows)
        n_cols = len(rows[0])

        gears = []

        for y in range(0, n_rows):
            for x in range(0, n_cols):
                cell = str(rows[y][x])

                if cell == "*":
                    adjacents = set()
                    for j in range(max(y - 1, 0), min(y + 1, len(rows) - 1) + 1):
                        for i in range(max(x - 1, 0), min(x + 1, len(rows[0]) - 1) + 1):
                            if str(rows[j][i]).isdigit():
                                adjacents.add(parse_number(rows, i, j))

                    if len(adjacents) == 2:
                        result = 1
                        for item in adjacents:
                            result *= item
                        gears.append(result)

        return sum(gears)


Day3()