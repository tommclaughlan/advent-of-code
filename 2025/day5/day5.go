package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"math"
	"slices"
	"strconv"
	"strings"
)

type Range struct {
	start int64
	end   int64
}

func (r Range) length() int {
	return int(r.end-r.start) + 1
}

func part1(input string) string {
	ranges, items := parseInput(input)

	fresh := make(map[int64]bool)

	for _, i := range items {
		for _, r := range ranges {
			if i >= r.start && i <= r.end {
				fresh[i] = true
			}
		}
	}

	return strconv.Itoa(countItems(fresh))
}

func part2(input string) string {
	ranges, _ := parseInput(input)

	slices.SortFunc(ranges, func(a, b Range) int {
		return int(a.start - b.start)
	})

	total := 0
	previous := Range{0, 0}

	for i, r := range ranges {
		newR := Range{r.start, r.end}
		for _, r2 := range ranges[i:] {
			if r2.start <= newR.end {
				newR = mergeRanges(newR, r2)
			} else {
				break
			}
		}
		if total == 0 || previous.end < newR.end {
			previous = newR
			total += newR.length()
		}
	}

	return strconv.Itoa(total)
}

func mergeRanges(first Range, second Range) Range {
	start := math.Min(float64(first.start), float64(second.start))
	end := math.Max(float64(first.end), float64(second.end))
	return Range{int64(start), int64(end)}
}

func countItems(items map[int64]bool) int {
	count := 0
	for range items {
		count += 1
	}
	return count
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
		Day:   "5",
	}

	runner.RunDay(day)
}
