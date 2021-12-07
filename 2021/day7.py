from util.runner import Runner
import numpy as np


def triangular_number(x):
    return (x * (x + 1)) / 2


class Day(Runner):
    def part1(self):
        pos = 0
        direction = -1
        crabs = next(self.input)
        last_sum = np.sum(crabs)

        while direction < 0:
            pos += 1
            new_sum = np.sum(np.abs(crabs - pos))
            if new_sum < last_sum:
                last_sum = new_sum
                direction = -1
            else:
                direction = 1

        return last_sum

    def part2(self):
        pos = 0
        direction = -1
        crabs = next(self.input)
        last_sum = np.sum(triangular_number(crabs))

        while direction < 0:
            pos += 1
            new_sum = np.sum(triangular_number(np.abs(crabs - pos)))
            if new_sum < last_sum:
                last_sum = new_sum
                direction = -1
            else:
                direction = 1

        return int(last_sum)


Day(7, lambda x: np.array([int(a.strip()) for a in x.split(',')]))
