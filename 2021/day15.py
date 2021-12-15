import math

from util.runner import Runner

import numpy as np


def get_neighbours(grid, node):
    neighbours = []

    if node[1] < grid.shape[1] - 1 and grid[node[0], node[1] + 1] > 0:
        neighbours.append((node[0], node[1] + 1))
    if node[1] > 0 and grid[node[0], node[1] - 1] > 0:
        neighbours.append((node[0], node[1] - 1))
    if node[0] < grid.shape[0] - 1 and grid[node[0] + 1, node[1]] > 0:
        neighbours.append((node[0] + 1, node[1]))
    if node[0] > 0 and grid[node[0] - 1, node[1]] > 0:
        neighbours.append((node[0] - 1, node[1]))

    return neighbours


def get_next_node(to_visit):
    smallest = ((0, 0), math.inf)
    for n, cost in to_visit:
        if cost < smallest[1]:
            smallest = (n, cost)
    return smallest


def find_path_cost(grid):
    costs = np.ones(grid.shape) * math.inf
    costs[0, 0] = 0
    to_visit = set()

    node = (0, 0)

    done = False

    while not done:
        neighbours = get_neighbours(grid, node)
        for n in neighbours:
            cost = costs[node] + grid[n]
            if cost < costs[n]:
                if (n, costs[n]) in to_visit:
                    to_visit.remove((n, costs[n]))
                costs[n] = cost
                to_visit.add((n, cost))
        grid[node] = -1

        next_node = get_next_node(to_visit)
        node = next_node[0]
        to_visit.remove(next_node)
        if node == (grid.shape[0] - 1, grid.shape[1] - 1):
            done = True
    return costs[grid.shape[0] - 1, grid.shape[1] - 1]


class Day(Runner):
    def part1(self):
        grid = np.row_stack([row for row in self.input])
        return find_path_cost(grid)

    def part2(self):
        grid = np.row_stack([row for row in self.input])

        x_size = grid.shape[1]
        y_size = grid.shape[0]

        big_grid = np.zeros((y_size * 5, x_size * 5))
        for x in range(5):
            for y in range(5):
                segment = grid.copy()
                segment += x + y
                segment[segment > 9] -= 9
                big_grid[y * y_size:(y + 1) * y_size, x * x_size:(x + 1) * x_size] = segment
        return find_path_cost(big_grid)


Day(15, lambda x: np.array([int(c) for c in x.strip()]))
