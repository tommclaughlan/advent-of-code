from util.runner import Runner


def get_hash(orig: str) -> int:
    sum = 0
    for char in orig:
        val = ord(char)
        sum += val
        sum *= 17
        sum %= 256
    return sum


class Lens:
    def __init__(self, label, power):
        self.label = label
        self.power = power

    def __eq__(self, other):
        return other.label == self.label


class Day15(Runner):
    def part1(self):
        values = []
        for line in self.input:
            for val in line.split(","):
                values.append(val)

        return sum([get_hash(x) for x in values])

    def part2(self):
        values = []
        for line in self.input:
            for val in line.split(","):
                values.append(val)

        hashmap: list[list[Lens]] = [[] for i in range(256)]

        for op in values:
            if "=" in op:
                [label, power] = op.split("=")
                hash = get_hash(label)
                lens = Lens(label, int(power))
                box = hashmap[hash]
                if lens in hashmap[hash]:
                    idx = hashmap[hash].index(lens)
                    hashmap[hash][idx] = lens
                else:
                    box.append(lens)
            elif "-" in op:
                label = op.split("-")[0]
                hash = get_hash(label)
                lens = Lens(label, 0)
                if lens in hashmap[hash]:
                    hashmap[hash].remove(lens)

        total = 0
        for i, box in enumerate(hashmap):
            for j, lens in enumerate(box):
                total += (i + 1) * (j + 1) * lens.power

        return total


Day15()
