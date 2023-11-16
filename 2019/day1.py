import math

from util.runner import Runner


def calculate_fuel(mass: int):
    return math.floor(mass / 3) - 2

def calculate_total_fuel(mass: int):
    total = 0
    added = True

    while added:
        fuel = calculate_fuel(mass)
        if fuel > 0:
            total += fuel
            mass = fuel
        else:
            added = False

    return total

class Day1(Runner):
    def part1(self):
        total_fuel = 0
        for line in self.input:
            mass = int(line)
            fuel = calculate_fuel(mass)
            total_fuel += fuel
        return total_fuel

    def part2(self):
        total_fuel = 0
        for line in self.input:
            mass = int(line)
            fuel = calculate_total_fuel(mass)
            total_fuel += fuel
        return total_fuel


Day1(int)
