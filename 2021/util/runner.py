from util.io import get_input


class Runner:
    def __init__(self, day, cast=str):
        self.cast = cast
        self.day = day

        self.run()

    def __getattr__(self, item):
        if item == 'input':
            return (self.cast(line) for line in get_input(self.day))
        raise AttributeError

    def part1(self):
        return NotImplementedError('not complete')

    def part2(self):
        return NotImplementedError('not complete')

    def run(self):
        print(f'Part 1: {self.part1()}')
        print(f'Part 2: {self.part2()}')
