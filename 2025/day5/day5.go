package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"strconv"
	"strings"
)

type Range struct {
	start int64
	end   int64
}

func part1(input string) string {
	ranges, items := parseInput(input)

	var fresh []int64

	for _, i := range items {
		for _, r := range ranges {
			if i >= r.start && i <= r.end {
				fresh = append(fresh, i)
			}
		}
	}

	return strconv.Itoa(len(fresh))
}

func part2(input string) string {
	return "Part 2"
}

func parseInput(input string) ([]Range, []int64) {
	lines := util.AsLines(input)

	var ranges []Range
	var items []int64
	processRanges := true

	for _, line := range lines {
		if processRanges {
			if line == "" {
				processRanges = false
				continue
			}
			ranges = append(ranges, parseRange(line))
		} else {
			items = append(items, parseInt(line))
		}
	}
	return ranges, items
}

func parseRange(row string) Range {
	split := strings.Split(row, "-")
	start, _ := strconv.ParseInt(split[0], 10, 64)
	end, _ := strconv.ParseInt(split[1], 10, 64)
	return Range{start, end}
}

func parseInt(row string) int64 {
	item, _ := strconv.ParseInt(row, 10, 64)
	return item
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "5_test",
	}

	runner.RunDay(day)
}
