from util.runner import Runner

import numpy as np


def x_fold(grid: 'np.ndarray[np.int]', coord):
    a = grid[:, :coord]
    b = grid[:, coord + 1:]

    for x in range(a.shape[1]):
        for y in range(a.shape[0]):
            a[y, coord - x - 1] = a[y, coord - x - 1] + b[y, x]

    return a


def y_fold(grid: 'np.ndarray[np.int]', coord):
    a = grid[:coord, :]
    b = grid[coord + 1:, :]

    for x in range(a.shape[1]):
        for y in range(a.shape[0]):
            a[coord - y - 1, x] = a[coord - y - 1, x] + b[y, x]

    return a


class Day(Runner):
    def parse_input(self):
        # just needs to be 'big enough' - the first couple of folds will give us the right size
        grid = np.zeros(shape=(1500, 1500))
        folds = []
        fill_grid = True
        for line in self.input:
            if line.strip() == "":
                fill_grid = False
                continue
            if fill_grid:
                coords = [int(c) for c in line.split(',')]
                grid[coords[1], coords[0]] = 1
            else:
                fold = line.split('fold along ')[1].split('=')
                folds.append(fold)

        return grid, folds

    def part1(self):
        grid, folds = self.parse_input()

        if folds[0][0] == 'x':
            grid = x_fold(grid, int(folds[0][1]))
        elif folds[0][0] == 'y':
            grid = y_fold(grid, int(folds[0][1]))

        return np.count_nonzero(grid[grid > 0])

    def part2(self):
        grid, folds = self.parse_input()

        for f in folds:
            if f[0] == 'x':
                grid = x_fold(grid, int(f[1]))
            elif f[0] == 'y':
                grid = y_fold(grid, int(f[1]))

        grid[grid > 0] = 1

        for y in range(grid.shape[0]):
            line = ''
            for x in range(grid.shape[1]):
                if grid[y, x] > 0:
                    line += '##'
                else:
                    line += '  '
            print(line)

        # this gives...
        return 'RHALRCRA'


Day(13)
