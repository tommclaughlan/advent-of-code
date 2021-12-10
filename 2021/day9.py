from util.runner import Runner
import numpy as np


def parse_grid(data):
    rows = []
    for line in data:
        rows.append(line)

    return np.row_stack([np.array(r) for r in rows])


def find_low_points(grid):
    output = []
    it = np.nditer(grid, flags=['multi_index'])
    for x in it:
        low = True
        idx = it.multi_index
        if idx[0] > 0:
            if grid[idx[0] - 1, idx[1]] - x <= 0:
                low = False
        if idx[1] > 0:
            if grid[idx[0], idx[1] - 1] - x <= 0:
                low = False
        if idx[0] < np.size(grid, 0) - 1:
            if grid[idx[0] + 1, idx[1]] - x <= 0:
                low = False
        if idx[1] < np.size(grid, 1) - 1:
            if grid[idx[0], idx[1] + 1] - x <= 0:
                low = False
        if low:
            output.append((int(x), idx))
    return output


def populate_basin(grid, basin):
    changes = False
    for x in basin:
        checked = x[1]
        if checked:
            continue
        idx = x[0]
        right = (idx[0] + 1, idx[1])
        left = (idx[0] - 1, idx[1])
        up = (idx[0], idx[1] - 1)
        down = (idx[0], idx[1] + 1)

        # need to track if we have checked a cell before, and also if we have added from another direction
        # this is ugly
        if [right, True] not in basin and [right, False] not in basin and right[0] < 100 and grid[right] < 9:
            changes = True
            basin.append([right, False])
        if [left, True] not in basin and [left, False] not in basin and left[0] >= 0 and grid[left] < 9:
            changes = True
            basin.append([left, False])
        if [up, True] not in basin and [up, False] not in basin and up[1] >= 0 and grid[up] < 9:
            changes = True
            basin.append([up, False])
        if [down, True] not in basin and [down, False] not in basin and down[1] < 100 and grid[down] < 9:
            changes = True
            basin.append([down, False])

        x[1] = True

    if not changes:
        return basin

    return populate_basin(grid, basin)


class Day(Runner):
    def part1(self):
        grid = parse_grid(self.input)

        lows = find_low_points(grid)
        idx = [low[1] for low in lows]

        return np.sum([grid[x] + 1 for x in idx])

    def part2(self):
        grid = parse_grid(self.input)

        lows = find_low_points(grid)
        basins = [len(populate_basin(grid, [[low[1], False]])) for low in lows]
        return np.product(sorted(basins)[-3:])


Day(9, lambda x: np.array([int(c) for c in x.strip()]))
