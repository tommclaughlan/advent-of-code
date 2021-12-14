from util.runner import Runner


def get_points(char):
    return {')': 3, ']': 57, '}': 1197, '>': 25137}[char]


def get_points_part_2(char):
    return {')': 1, ']': 2, '}': 3, '>': 4}[char]


def is_open(char):
    return char == '(' or char == '[' or char == '{' or char == '<'


def is_close(char):
    return char == ')' or char == ']' or char == '}' or char == '>'


def get_closing(char):
    return {'(': ')', '[': ']', '{': '}', '<': '>'}[char]


def is_match(opening, close):
    return close == get_closing(opening)


class Day(Runner):
    def part1(self):
        score = 0
        for line in self.input:
            stack = []
            for char in line:
                if is_close(char) and not is_match(stack.pop(), char):
                    score += get_points(char)
                    break
                elif is_open(char):
                    stack.append(char)

        return score

    def part2(self):
        scores = []
        for line in self.input:
            stack = []

            incomplete = True
            for char in line:
                if is_close(char) and not is_match(stack.pop(), char):
                    incomplete = False
                    break
                elif is_open(char):
                    stack.append(char)

            if not incomplete:
                continue

            completion = ''
            while len(stack) > 0:
                completion += get_closing(stack.pop())

            score = 0
            for char in completion:
                score *= 5
                score += get_points_part_2(char)

            scores.append(score)

        return sorted(scores)[int(len(scores) / 2)]


Day(10)
