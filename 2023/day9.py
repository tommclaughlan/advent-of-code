from util.runner import Runner


def extrapolate(series: list[int]):
    next_layer = series
    levels = [series]
    while True:
        diff = get_differences(next_layer)
        if len([x for x in diff if x != 0]) == 0:
            break
        else:
            levels.append(diff)
            next_layer = diff

    for i in range(len(levels), 1, -1):
        level = levels[i - 1]
        to_add = level[-1]
        to_subtract = level[0]
        levels[i - 2].insert(0, levels[i - 2][0] - to_subtract)
        levels[i - 2].append(levels[i - 2][-1] + to_add)

    return levels[0][-1], levels[0][0]


def get_differences(series: list[int]):
    diff = []
    for i in range(1, len(series)):
        diff.append(series[i] - series[i - 1])
    return diff


class Day9(Runner):
    def part1(self):
        nexts = [extrapolate([int(l) for l in line.split()])[0] for line in self.input]
        return sum(nexts)

    def part2(self):
        nexts = [extrapolate([int(l) for l in line.split()])[1] for line in self.input]
        return sum(nexts)


Day9()
