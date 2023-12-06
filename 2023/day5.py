from util.runner import Runner


def parse_seeds(line):
    return [int(x) for x in line.split("seeds: ")[1].split(" ")]


def parse_input(puzzle_input):
    seeds = []
    maps = {}
    order = []

    current_category = ""
    current_map = {}

    for line in puzzle_input:
        if str(line).startswith("seeds:"):
            seeds = parse_seeds(line)
        else:
            if str(line) == "":
                if current_category != "":
                    maps[current_category] = current_map
                current_map = {}
            elif "map" in str(line):
                current_category = line.split(" ")[0]
                order.append(current_category)
            else:
                parts = line.split(" ")
                current_map[int(parts[1])] = {'dest': int(parts[0]), 'range': int(parts[2])}

    maps[current_category] = current_map

    return seeds, maps, order


def split_range(start, end, rule):
    rs, re, ds = rule

    lhs = []
    mapped = []
    rhs = []

    if re < start or rs > end:
        return [(start, end)], []
    else:
        offset = start - rs
        mapped_start = ds + offset
        seed_range = end - start
        rule_range = re - rs

        if rs <= start:
            if re >= end:
                # mapping the whole range
                mapped = [(mapped_start, mapped_start + seed_range)]
            else:
                # mapping from the start to somewhere in the middle
                mapped_range = re - start
                rhs = [(re + 1, end)]
                mapped = [(mapped_start, mapped_start + mapped_range)]

        if start < rs <= end:
            lhs = [(start, rs - 1)]
            if re <= end:
                mapped = [(ds, ds + rule_range)]
                if re != end:
                    rhs = [(re + 1, end)]
            else:
                mapped = [(ds, ds + seed_range + offset)]

    return lhs + rhs, mapped


class Day5(Runner):
    def part1(self):
        seeds, maps, order = parse_input(self.input)

        locations = []

        for seed in seeds:
            val = new_val = seed
            for op in order:
                mapper = maps[op]
                changed = False
                for low in mapper.keys():
                    if low <= val < low + mapper[low]['range']:
                        dest = mapper[low]['dest']
                        above_range = val - low
                        new_val = dest + above_range
                        changed = True
                        break
                if changed:
                    val = new_val

            locations.append(val)

        return min(locations)

    def part2(self):
        raw_seeds, maps, order = parse_input(self.input)

        ranges = [(raw_seeds[2*i], raw_seeds[2*i] + raw_seeds[(2*i)+1] - 1) for i in range(0, int(len(raw_seeds) / 2))]
        todo = []

        for op in order:
            mapper = maps[op]
            processing = ranges + todo
            new_ranges = []
            for low in mapper.keys():
                rs = low
                re = low + mapper[low]['range'] - 1
                rd = mapper[low]['dest']
                todo = []
                for start, end in processing:
                    unmapped, mapped = split_range(start, end, (rs, re, rd))
                    new_ranges += mapped
                    todo += unmapped
                processing = todo
            ranges = new_ranges

        return min([x[0] for x in ranges + todo])


Day5()
