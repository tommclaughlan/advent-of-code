package main

import (
	"2025/runner"
	"2025/types"
)

func part1(input string) string {
	return "Part 1"
}

func part2(input string) string {
	return "Part 2"
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "1",
	}

	runner.RunDay(day)
}
