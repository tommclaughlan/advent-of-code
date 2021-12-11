from util.runner import Runner

import numpy as np


def time_series(grid, steps):
    grids = [grid]
    for step in range(steps):
        next_grid = grids[step] + 1
        next_grid[next_grid > 9] = 0
        coords = np.where(next_grid == 0)
        flashes = list(zip(coords[0], coords[1]))
        while len(flashes) > 0:
            next_grid[next_grid == 0] = -1
            for flash in flashes:
                local = next_grid[
                        max(flash[0] - 1, 0):min(flash[0] + 2, 99),
                        max(flash[1] - 1, 0):min(flash[1] + 2, 99)]
                local[local > 0] += 1
                local[local > 9] = 0

            coords = np.where(next_grid == 0)
            flashes = list(zip(coords[0], coords[1]))
        next_grid[next_grid < 0] = 0
        grids.append(next_grid)

    return grids


class Day(Runner):
    def get_grid(self):
        rows = [[int(c) for c in line.strip()] for line in self.input]
        return np.row_stack([np.array(r) for r in rows])

    def part1(self):
        grid = self.get_grid()
        grids = np.array(time_series(grid, 100))
        return np.count_nonzero(grids == 0)

    def part2(self):
        grid = self.get_grid()
        step = 0
        while np.count_nonzero(grid == 0) < 100:
            step += 1
            grid = time_series(grid, 1)[1]
        return step


Day(11)
