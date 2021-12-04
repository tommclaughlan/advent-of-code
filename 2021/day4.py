from util.runner import Runner
import numpy as np


class BingoCard:
    def __init__(self):
        self.rows = []
        self.card: type(np.ndarray) = np.ndarray([])

    def set_row(self, row):
        self.rows.append(row)

    def build_card(self):
        self.card = np.row_stack([np.array(r) for r in self.rows])

    def mark_card(self, number):
        if number in self.card:
            self.card[self.card == number] = -1

    def check_card(self):
        for row in self.card:
            if len([i for i in row if i >= 0]) == 0:
                return True
        for col in self.card.transpose():
            if len([i for i in col if i >= 0]) == 0:
                return True
        return False

    def get_score(self):
        # since we're using -1 to track removed elements
        # replace with 0 to avoid messing up the sum
        self.card[self.card == -1] = 0
        return self.card.sum()


class Day(Runner):
    def parse(self):
        cards = []
        buffer = None
        numbers = None
        for line in self.input:
            if numbers is None:
                numbers = [int(n) for n in line.split(',')]
                continue
            if line == "":
                if buffer is not None:
                    buffer.build_card()
                    cards.append(buffer)
                buffer = BingoCard()
            else:
                buffer.set_row([int(n) for n in line.split(' ') if n.strip() != ''])

        buffer.build_card()
        cards.append(buffer)

        return cards, numbers

    def part1(self):
        cards, numbers = self.parse()
        for n in numbers:
            for card in cards:
                card.mark_card(n)
                if card.check_card():
                    return n * card.get_score()

    def part2(self):
        cards, numbers = self.parse()
        for n in numbers:
            for card in cards:
                card.mark_card(n)
                if card.check_card():
                    cards.remove(card)
                if len(cards) == 1:
                    return n * card.get_score()


Day(4, lambda l: l.strip())
