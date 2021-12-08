from util.runner import Runner
import numpy as np


def find_zero(digits, one, eight, nine) -> set:
    for x in digits:
        if len(x) != 6:
            continue
        diff = x.symmetric_difference(eight)
        if len(diff) == 1 and diff.pop() not in one and x is not nine:
            return x
    raise Exception("Failed to find zero")


def find_one(digits) -> set:
    return [x for x in digits if len(x) == 2][0]


def find_four(digits) -> set:
    return [x for x in digits if len(x) == 4][0]


def find_six(digits, zero, nine) -> set:
    return [x for x in digits if len(x) == 6 and x is not zero and x is not nine][0]


def find_seven(digits) -> set:
    return [x for x in digits if len(x) == 3][0]


def find_eight(digits) -> set:
    return [x for x in digits if len(x) == 7][0]


def find_nine(digits, four, seven) -> set:
    nine = [x for x in digits if seven.issubset(x) and four.issubset(x) and len(x) == 6]
    return nine[0]


class Day(Runner):
    def part1(self):
        count = 0
        for line in self.input:
            output = line.split('|')[1].strip()
            digits = np.array(output.split(' '))
            ones = [x for x in digits if len(x) == 2]
            fours = [x for x in digits if len(x) == 4]
            sevens = [x for x in digits if len(x) == 3]
            eights = [x for x in digits if len(x) == 7]
            count += len(ones) + len(fours) + len(sevens) + len(eights)

        return count

    def part2(self):
        total = 0
        for line in self.input:
            parts = line.split('|')
            scramble = np.array([set(x) for x in parts[0].strip().split(' ')])
            digits = np.array([set(x) for x in parts[1].strip().split(' ')])
            one = find_one(scramble)
            seven = find_seven(scramble)
            a = [x for x in seven if x not in one][0]
            four = find_four(scramble)
            eight = find_eight(scramble)
            nine = find_nine(scramble, four, seven)
            e = nine.symmetric_difference(eight).pop()
            g = nine.symmetric_difference(four.union(seven)).pop()
            zero = find_zero(scramble, one, eight, nine)
            d = eight.symmetric_difference(zero).pop()
            b = [x for x in four.symmetric_difference(one) if x != d][0]
            six = find_six(scramble, zero, nine)
            c = eight.symmetric_difference(six).pop()
            f = [x for x in one if x is not c][0]
            two = {a, c, d, e, g}
            three = {a, c, d, f, g}
            five = {a, b, d, f, g}
            matchers = [zero, one, two, three, four, five, six, seven, eight, nine]

            number = 0
            digit_pos = 3

            for digit in digits:
                number += matchers.index(digit) * (10 ** digit_pos)
                digit_pos -= 1

            total += number

        return total


Day(8)
