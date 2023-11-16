from util.intcode import Intcode
from util.runner import Runner


class Day2(Runner):
    def part1(self):
        line = next(self.input)
        code = list(map(int, line.split(",")))

        program = Intcode(code)

        program.modify(1, 12)
        program.modify(2, 2)
        return program.run()

    def part2(self):
        line = next(self.input)
        code = list(map(int, line.split(",")))

        program = Intcode(code)

        for noun in range(0, 100):
            for verb in range(0, 100):
                program.load(list(map(int, line.split(","))))
                program.modify(1, noun)
                program.modify(2, verb)

                result = program.run()
                if result == 19690720:
                    return 100 * noun + verb

        return 1


Day2()
