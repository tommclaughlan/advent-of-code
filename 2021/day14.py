from collections import Counter

from util.runner import Runner


class Day(Runner):
    def parse_input(self):
        data = self.input

        polymer = next(data)
        _ = next(data)  # throw away the blank line

        replacements = {}

        for i in data:
            parts = i.split(' -> ')
            pair = parts[0]
            to_insert = parts[1]
            replacements[pair] = to_insert

        counts = {}
        for i in range(len(polymer) - 1):
            pair = polymer[i:i + 2]
            if pair in counts:
                counts[pair] += 1
            else:
                counts[pair] = 1

        return polymer, counts, replacements

    def run_steps(self, steps):
        polymer, pairs, replacements = self.parse_input()
        for i in range(steps):
            new_pairs = {}
            for pair, v in pairs.items():
                to_insert = replacements[pair]
                p1 = pair[0] + to_insert
                p2 = to_insert + pair[1]
                new_pairs[p1] = new_pairs.get(p1, 0) + v
                new_pairs[p2] = new_pairs.get(p2, 0) + v
            pairs = new_pairs

        counts = {polymer[-1]: 1}
        for pair, v in pairs.items():
            counts[pair[0]] = counts.get(pair[0], 0) + v

        return max(counts.values()) - min(counts.values())

    def part1(self):
        return self.run_steps(10)

    def part2(self):
        return self.run_steps(40)


Day(14)
