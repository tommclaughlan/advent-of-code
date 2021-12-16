import math

from typing import Tuple

from util.runner import Runner

from bitstring import BitArray


class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

    def get_value(self):
        raise NotImplementedError

    def get_version(self):
        raise NotImplementedError


class Literal(Packet):
    def __init__(self, version, type_id, value):
        super(Literal, self).__init__(version, type_id)
        self.value = value

    def __str__(self):
        return "Literal: " + str(self.value)

    def get_value(self):
        return self.value

    def get_version(self):
        return self.version


class Operator(Packet):
    def __init__(self, version, type_id, sub_packets):
        super(Operator, self).__init__(version, type_id)
        self.sub_packets = sub_packets

    def get_version(self):
        return sum(p.get_version() for p in self.sub_packets) + self.version

    def get_value(self):
        raise NotImplementedError


class Sum(Operator):
    def get_value(self):
        return sum(p.get_value() for p in self.sub_packets)


class Product(Operator):
    def get_value(self):
        return math.prod(p.get_value() for p in self.sub_packets)


class Minimum(Operator):
    def get_value(self):
        return min(p.get_value() for p in self.sub_packets)


class Maximum(Operator):
    def get_value(self):
        return max(p.get_value() for p in self.sub_packets)


class Greater(Operator):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() > self.sub_packets[1].get_value() else 0


class Lesser(Operator):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() < self.sub_packets[1].get_value() else 0


class Equal(Operator):
    def get_value(self):
        return 1 if self.sub_packets[0].get_value() == self.sub_packets[1].get_value() else 0


def parse_literal(data):
    literal = ""
    cursor = 0
    while True:
        chunk = data[cursor:cursor + 5]
        literal += chunk[1:]
        cursor += 5
        if chunk[0] == '0':
            return BitArray(bin=literal).uint, cursor


def read_n_packets(data, n):
    packets = []
    bits_read = 0
    while len(packets) < n:
        packet, read = read_packet(data[bits_read:])
        bits_read += read
        packets.append(packet)
    return packets, bits_read


def read_sub_packets(data):
    cursor = 0
    packets = []
    while cursor < len(data):
        packet, bits_read = read_packet(data[cursor:])
        packets.append(packet)
        cursor += bits_read
    return packets, cursor


def read_packet(data) -> Tuple[Packet, int]:
    version = BitArray(bin=data[:3]).uint
    type_id = BitArray(bin=data[3:6]).uint
    if type_id == 4:  # literal
        literal, bits_read = parse_literal(data[6:])
        return Literal(version, type_id, literal), bits_read + 6  # add headers
    else:  # operator
        length_type_id = int(data[6])
        sub_packets = []
        bits_read = 0
        if length_type_id == 0:
            length = BitArray(bin=data[7:22]).uint
            sub_packets, bits_read = read_sub_packets(data[22:length + 22])
            bits_read += 22  # add headers
        elif length_type_id == 1:
            n_packets = BitArray(bin=data[7:18]).uint
            sub_packets, bits_read = read_n_packets(data[18:], n_packets)
            bits_read += 18  # add headers
        ctor = Operator

        if type_id == 0:
            ctor = Sum
        elif type_id == 1:
            ctor = Product
        elif type_id == 2:
            ctor = Minimum
        elif type_id == 3:
            ctor = Maximum
        elif type_id == 5:
            ctor = Greater
        elif type_id == 6:
            ctor = Lesser
        elif type_id == 7:
            ctor = Equal
        return ctor(version, type_id, sub_packets), bits_read


class Day(Runner):
    def part1(self):
        line = next(self.input)
        bits = "".join([BitArray(hex=c).bin for c in line])
        packet, bits_read = read_packet(bits)
        return packet.get_version()

    def part2(self):
        line = next(self.input)
        bits = "".join([BitArray(hex=c).bin for c in line])
        packet, bits_read = read_packet(bits)
        return packet.get_value()


Day(16)
