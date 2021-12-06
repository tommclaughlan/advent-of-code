from util.runner import Runner
import numpy as np


class Day(Runner):
    def count_fish(self, days):
        data = next(self.input)

        key, val = np.unique(data, return_counts=True)
        population = [0] * 9
        for i in key:
            population[i] = val[i - 1]
        for day in range(days):
            to_spawn = population[0]
            population = population[1:] + [to_spawn]
            population[6] = population[6] + to_spawn

        return sum(population)

    def part1(self):
        return self.count_fish(80)

    def part2(self):
        return self.count_fish(256)


Day(6, lambda x: [int(a.strip()) for a in x.split(',')])
