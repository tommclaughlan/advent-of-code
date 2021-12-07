from util.runner import Runner
import numpy as np


def triangular_number(x):
    return (x * (x + 1)) / 2


class Day(Runner):
    def part1(self):
        pos = 0
        crabs = next(self.input)
        last_sum = np.sum(crabs)

        while True:
            pos += 1
            new_sum = np.sum(np.abs(crabs - pos))
            if new_sum < last_sum:
                last_sum = new_sum
            else:
                break

        return last_sum

    def part2(self):
        pos = 0
        crabs = next(self.input)
        last_sum = np.sum(triangular_number(crabs))

        while True:
            pos += 1
            new_sum = np.sum(triangular_number(np.abs(crabs - pos)))
            if new_sum < last_sum:
                last_sum = new_sum
            else:
                break

        return int(last_sum)


Day(7, lambda x: np.array([int(a.strip()) for a in x.split(',')]))
