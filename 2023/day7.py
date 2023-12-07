from functools import cmp_to_key
from itertools import product

from util.runner import Runner


def get_value(card: str, part=1):
    if card.isdigit():
        return int(card)

    if card == 'T':
        return 10
    if card == 'J':
        if part == 2:
            return 1
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14


def compare_same_hand(a: str, b: str, part=1):
    for i in range(0, len(a)):
        if a[i] != b[i]:
            if get_value(a[i], part) > get_value(b[i], part):
                return 1
            else:
                return -1

    return 0


def compare_hands(a: (str, int), b: (str, int)):
    val_a = get_hand_value(a[0])
    val_b = get_hand_value(b[0])

    if val_a > val_b:
        return 1
    elif val_a < val_b:
        return -1
    else:
        return compare_same_hand(a[2], b[2])

def compare_hands_2(a: (str, int), b: (str, int)):
    val_a = get_hand_value(a[0])
    val_b = get_hand_value(b[0])

    if val_a > val_b:
        return 1
    elif val_a < val_b:
        return -1
    else:
        return compare_same_hand(a[2], b[2], 2)


def get_hand_value(hand: str):
    map = {}

    for c in hand:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    if map.keys() == 5:
        return 1

    sorted_counts = sorted(map.values())

    if sorted_counts == [1, 1, 1, 2]:
        return 2

    if sorted_counts == [1, 2, 2]:
        return 3

    if sorted_counts == [1, 1, 3]:
        return 4

    if sorted_counts == [2, 3]:
        return 5

    if sorted_counts == [1, 4]:
        return 6

    if sorted_counts == [5]:
        return 7

    return 0

class Day7(Runner):
    def part1(self):

        hands = []

        for line in self.input:
            parts = line.split()
            hands.append((parts[0], int(parts[1]), parts[0]))

        sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

        return sum([(i+1)*x[1] for i, x in enumerate(sorted_hands)])

    def part2(self):
        hands = []

        for line in self.input:
            parts = line.split()
            hands.append((parts[0], int(parts[1]), parts[0]))

        values = 'AKQT98765432'

        for i, hand in enumerate(hands):
            current_best = hand[0]
            j_count = hand[2].count("J")
            if j_count > 0:
                j_perms = product(values, repeat=j_count)
                for perm in j_perms:
                    new_hand = hand[2]
                    for p in perm:
                        j_idx = new_hand.index("J")
                        new_hand = new_hand[:j_idx] + p + new_hand[j_idx+1:]
                    if compare_hands((new_hand, 0, new_hand), (current_best, 0, current_best)) > 0:
                        current_best = new_hand
            hands[i] = (current_best, hand[1], hand[2])

        sorted_hands = sorted(hands, key=cmp_to_key(compare_hands_2))

        return sum([(i+1)*x[1] for i, x in enumerate(sorted_hands)])


Day7()
