package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"strconv"
)

func part1(input string) string {
	lines := util.AsLines(input)

	total := 0

	for _, line := range lines {
		startIdx, first := findFirstLargest(line[:len(line)-1])
		_, second := findFirstLargest(line[startIdx+1:])

		total += (10 * first) + second
	}

	return strconv.Itoa(total)
}

func part2(input string) string {
	return "Part 2"
}

func findFirstLargest(value string) (int, int) {
	largest := 0
	largestIdx := -1
	for i, char := range value {
		val, _ := strconv.Atoi(string(char))
		if val > largest {
			largest = val
			largestIdx = i
		}
	}
	return largestIdx, largest
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "3",
	}

	runner.RunDay(day)
}
