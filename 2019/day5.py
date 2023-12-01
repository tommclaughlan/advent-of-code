from util.intcode import Intcode
from util.runner import Runner


class Day5(Runner):
    def part1(self):
        line = next(self.input)
        code = list(map(int, line.split(",")))

        program = Intcode(code)
        program.return_output()
        program.input = 1
        return program.run()

    def part2(self):
        line = next(self.input)
        code = list(map(int, line.split(",")))

        program = Intcode(code)
        program.return_output()
        program.input = 5
        return program.run()


Day5()
