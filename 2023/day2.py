from util.runner import Runner


def map_round(round: str):
    colours = {'red': 0, 'green': 0, 'blue': 0}

    for draws in round:
        for draw in draws.strip().split(", "):
            col = draw.split(" ")
            if col[1] == 'red':
                if int(col[0]) > colours['red']:
                    colours['red'] = int(col[0])
            if col[1] == 'green':
                if int(col[0]) > colours['green']:
                    colours['green'] = int(col[0])
            if col[1] == 'blue':
                if int(col[0]) > colours['blue']:
                    colours['blue'] = int(col[0])

    return colours


class Day2(Runner):
    def part1(self):
        reds = 12
        greens = 13
        blues = 14

        sum = 0

        # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        for idx, line in enumerate(self.input):
            rounds_raw = line.split(":")[1].strip().split(";")
            rounds = map_round(rounds_raw)
            if rounds['red'] <= reds and rounds['green'] <= greens and rounds['blue'] <= blues:
                sum += idx + 1

        return sum

    def part2(self):
        sum = 0
        for idx, line in enumerate(self.input):
            rounds_raw = line.split(":")[1].strip().split(";")
            rounds = map_round(rounds_raw)
            reds = rounds['red']
            greens = rounds['green']
            blues = rounds['blue']

            sum += reds * greens * blues

        return sum


Day2()
