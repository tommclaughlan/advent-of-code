import math

from util.runner import Runner


def parse_input(lines):
    moves = ''
    nodes = {}

    for i, line in enumerate(lines):
        if i == 0:
            moves = line
        elif i > 1:
            parts = line.split(' = ')
            targets = parts[1][1:-1].split(', ')
            nodes[parts[0]] = (targets[0], targets[1])

    return moves, nodes


class Day8(Runner):
    def part1(self):
        instructions, nodes = parse_input(self.input)
        ins_idx = 0

        current_node = 'AAA'

        moves = 0

        while current_node != 'ZZZ':
            ins = instructions[ins_idx]
            ins_idx += 1
            if ins_idx == len(instructions):
                ins_idx = 0
            next_idx = 0 if ins == 'L' else 1
            current_node = nodes[current_node][next_idx]
            moves += 1

        return moves

    def part2(self):

        instructions, nodes = parse_input(self.input)

        ghosts = {}

        for node in nodes:
            if node[2] == 'A':
                ghosts[node] = [node, [], 0]

        for ghost in ghosts.values():
            new_step = True
            steps = 0
            while new_step:
                new_step = False

                for ins_idx, ins in enumerate(instructions):
                    next_idx = 0 if ins == 'L' else 1
                    node = nodes[ghost[0]]
                    next_node = node[next_idx]
                    steps += 1
                    if next_node[2] == 'Z' and ghost[2] == 0:
                        ghost[2] = steps
                        new_step = False
                        break
                    if (next_node, ins_idx) not in ghost[1]:
                        ghost[0] = next_node
                        ghost[1].append((next_node, ins_idx))
                        new_step = True

        return math.lcm(*[len(x[1]) + 1 for x in ghosts.values()])


Day8()
