from util.runner import Runner


class Day(Runner):
    def part1(self):
        h = 0
        d = 0

        for parts in self.input:
            cmd = parts[0]
            amount = int(parts[1])

            if cmd == 'forward':
                h += amount
            elif cmd == 'down':
                d += amount
            elif cmd == 'up':
                d -= amount

        return h * d

    def part2(self):
        h = 0
        d = 0
        a = 0

        for parts in self.input:
            cmd = parts[0]
            amount = int(parts[1])

            if cmd == 'forward':
                h += amount
                d += a * amount
            elif cmd == 'down':
                a += amount
            elif cmd == 'up':
                a -= amount

        return h * d


Day(2, lambda l: l.split(' '))
