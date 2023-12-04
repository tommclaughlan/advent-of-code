from util.runner import Runner


def parse_games(input):
    games = []
    for line in input:
        cards = line.split(":")[1].strip()
        sides = [x.strip() for x in cards.split("|")]
        winning = [int(x) for x in sides[0].split()]
        own_numbers = [int(x) for x in sides[1].split()]
        games.append([winning, own_numbers])
    return games


class Day4(Runner):
    def part1(self):
        games = parse_games(self.input)

        score = 0

        for game in games:
            matches = 0
            for n in game[0]:
                if n in game[1]:
                    matches += 1

            if matches > 0:
                score += 2**(matches - 1)

        return score

    def part2(self):
        games = parse_games(self.input)

        cards = [1 for _ in games]

        for idx, game in enumerate(games):
            matches = 0
            for n in game[0]:
                if n in game[1]:
                    matches += 1
            for copy in range(0, matches):
                cards[idx + copy + 1] += cards[idx]

        return sum(cards)


Day4()
