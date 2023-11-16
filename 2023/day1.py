from util.runner import Runner


class Day(Runner):
    def part1(self):
        previous = -1
        count = 0

        for depth in self.input:
            if depth > previous > 0:
                count += 1

            previous = depth

        return count

    def part2(self):
        prev = -1
        prev2 = -1
        prev3 = -1
        count = 0

        for depth in self.input:
            prev_window = prev3 + prev2 + prev
            current_window = prev2 + prev + depth

            if current_window > prev_window and prev3 > 0:
                count += 1

            prev3 = prev2
            prev2 = prev
            prev = depth

        return count


Day(1, int)
