from util.runner import Runner


class Day1(Runner):
    def part1(self):
        calibrations = []

        for line in self.input:
            digits_in_line = []
            for c in filter(str.isdigit, line):
                digits_in_line.append(c)

            calibrations.append(int(digits_in_line[0] + digits_in_line[-1]))

        return sum(calibrations)

    def part2(self):
        numbers = {
            'one': 'o1e',
            'two': 't2o',
            'three': 'thr3e',
            'four': 'fo4r',
            'five': 'fi5e',
            'six': 's6x',
            'seven': 'se7en',
            'eight': 'ei8ht',
            'nine': 'ni9e'
        }

        calibrations = []

        for line in self.input:
            digits_in_line = []

            processed_line = line

            for i, (k, v) in enumerate(numbers.items()):
                processed_line = str.replace(processed_line, k, v)

            for c in filter(str.isdigit, processed_line):
                digits_in_line.append(c)

            calibrations.append(int(digits_in_line[0] + digits_in_line[-1]))

        return sum(calibrations)


Day1()
