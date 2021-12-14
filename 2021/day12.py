from util.runner import Runner


def get_connected(connections, node):
    for i in connections:
        if node != 'start' and (i[0] == 'start' or i[1] == 'start'):
            continue

        if node == i[0]:
            yield i[1]
        elif node == i[1]:
            yield i[0]


def get_paths(connections):
    paths = [['start']]
    done_paths = []
    while True:
        next_paths = []
        for i in paths:
            for n in get_connected(connections, i[-1]):
                if n == 'end':
                    done_paths.append(i + [n])
                elif n.isupper() or (n.islower() and n not in i):
                    next_paths.append(i + [n])
        if len(next_paths) == 0:
            return done_paths
        else:
            paths = next_paths


def validate_node(path: list, next_node):
    for n in path:
        if n.islower() and path.count(n) > 1 and next_node in path:
            return False

    return True


def get_paths_part2(connections):
    paths = [['start']]
    done_paths = []
    while True:
        next_paths = []
        for i in paths:
            for n in get_connected(connections, i[-1]):
                if n == 'end':
                    done_paths.append(i + [n])
                elif n.isupper() or validate_node(i, n):
                    next_paths.append(i + [n])
        if len(next_paths) == 0:
            return done_paths
        else:
            paths = next_paths


class Day(Runner):
    def part1(self):
        connections = []
        for c in self.input:
            connections.append(c.split('-'))

        paths = get_paths(connections)

        return len(paths)

    def part2(self):
        connections = []
        for c in self.input:
            connections.append(c.split('-'))

        paths = get_paths_part2(connections)

        return len(paths)


Day(12)
