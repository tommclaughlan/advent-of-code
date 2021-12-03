from util.runner import Runner
from bitstring import BitArray


def most_common_bits(array):
    n_bits = None
    bit_count = []

    for b in array:
        if n_bits is None:
            n_bits = len(b.bin)
            bit_count = [0] * n_bits
        for i in range(0, n_bits):
            if b.uint & (2 ** i) > 0:
                bit_count[i] += 1
            else:
                bit_count[i] -= 1
    bit_count.reverse()
    return bit_count


def reduce_list(data, bit, most):
    bit_count = most_common_bits(data)
    bitmask = str((not most) ^ (1 if bit_count[bit] >= 0 else 0))
    return [d for d in data if d.bin[bit] != bitmask]


class Day(Runner):
    def part1(self):
        bit_count = most_common_bits(self.input)

        gamma = BitArray(bin="".join('1' if c > 0 else '0' for c in bit_count))
        epsilon = ~gamma
        return gamma.uint * epsilon.uint

    def part2(self):
        n_bits = len(next(self.input).bin)

        oxy = [line for line in self.input]
        co2 = [line for line in self.input]

        for bit in range(0, n_bits):
            if len(oxy) > 1:
                oxy = reduce_list(oxy, bit, True)
            if len(co2) > 1:
                co2 = reduce_list(co2, bit, False)

        return oxy[0].uint * co2[0].uint


Day(3, lambda s: BitArray(bin=s))
