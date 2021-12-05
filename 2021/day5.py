from util.runner import Runner
import numpy as np


def fill_vents(row, vents):
    y1 = row[0, 1]
    y2 = row[1, 1]
    x1 = row[0, 0]
    x2 = row[1, 0]

    diag = False
    anti_diag = False

    if x1 != x2 and y1 != y2:
        diag = True
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            anti_diag = True

    # sort the coordinates so we are selecting low_i:high_i
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 > x2:
        x1, x2 = x2, x1

    if diag:
        if anti_diag:
            # anti-diagonal -> select area, flip, fill diag
            selection = np.fliplr(vents[y1:y2 + 1, x1:x2 + 1])
            np.fill_diagonal(selection, selection.diagonal() + 1)
        else:
            # diagonal -> select area, fill diag
            selection = vents[y1:y2 + 1, x1:x2 + 1]
            np.fill_diagonal(selection, selection.diagonal() + 1)
    else:
        # horizontal or vertical, just fill it all
        vents[y1:y2 + 1, x1:x2 + 1] = vents[y1:y2 + 1, x1:x2 + 1] + 1


def create_map(data, part2=False):
    max_x = 1000
    max_y = 1000

    vents = np.zeros((max_x, max_y))

    for row in data:
        if part2:
            fill_vents(row, vents)
        elif row[0, 0] == row[1, 0] or row[0, 1] == row[1, 1]:
            fill_vents(row, vents)

    return vents


class Day(Runner):
    def part1(self):
        lines = create_map(self.input)
        return np.count_nonzero(lines > 1)

    def part2(self):
        lines = create_map(self.input, True)
        return np.count_nonzero(lines > 1)


Day(5, lambda x: np.array([(int(p.split(',')[0]), int(p.split(',')[1])) for p in x.strip().split(' -> ')]))
