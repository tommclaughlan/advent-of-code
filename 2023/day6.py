from functools import reduce

from util.runner import Runner


def parse_input(input):

    lines = [str(line).split()[1:] for line in input]

    times = [int(x) for x in lines[0]]
    distances = [int(x) for x in lines[1]]

    return times, distances


class Day6(Runner):
    def part1(self):
        times, distances = parse_input(self.input)

        wins = []

        for i in range(0, len(times)):
            time = times[i]
            distance = distances[i]
            wins.append(0)
            for t in range(1, time):
                move_time = time - t
                speed = t
                new_distance = speed * move_time
                if new_distance > distance:
                    wins[i] += 1

        return reduce(lambda x, y: x*y, wins)

    def part2(self):
        times, distances = parse_input(self.input)
        time = int(''.join([str(x) for x in times]))
        distance = int(''.join([str(x) for x in distances]))

        first_win = 0
        last_win = time

        for t in range(1, time):
            move_time = time - t
            speed = t
            new_distance = speed * move_time
            if new_distance > distance:
                first_win = t
                break

        for t in range(time, 1, -1):
            move_time = time - t
            speed = t
            new_distance = speed * move_time
            if new_distance > distance:
                last_win = t
                break

        return last_win - first_win + 1


Day6()
