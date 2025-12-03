package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"math"
	"strconv"
)

func part1(input string) string {
	lines := util.AsLines(input)

	total := 0
	batterySize := 2

	for _, line := range lines {
		total += findBattery(line, 0, batterySize-1)
	}

	return strconv.Itoa(total)
}

func part2(input string) string {
	lines := util.AsLines(input)

	total := 0
	batterySize := 12

	for _, line := range lines {
		total += findBattery(line, 0, batterySize-1)
	}

	return strconv.Itoa(total)
}

func findBattery(value string, battery int, pos int) int {
	largest := 0
	largestIdx := -1
	for i, char := range value[:len(value)-pos] {
		val, _ := strconv.Atoi(string(char))
		if val > largest {
			largest = val
			largestIdx = i
		}
	}
	battery += largest * int(math.Pow10(pos))
	if pos == 0 {
		return battery
	}
	return findBattery(value[largestIdx+1:], battery, pos-1)
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "3",
	}

	runner.RunDay(day)
}
