package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"strconv"
)

func part1(input string) string {
	lines := util.AsLines(input)

	commands := parseLines(lines)

	point := 50
	total := 0

	for _, command := range commands {
		value, _ := strconv.Atoi(command[1])
		if command[0] == "R" {
			point += value
		}
		if command[0] == "L" {
			point -= value
		}
		if point%100 == 0 {
			total += 1
		}
	}

	return strconv.Itoa(total)
}

func part2(input string) string {
	lines := util.AsLines(input)

	commands := parseLines(lines)

	point := 50
	total := 0

	for _, command := range commands {
		value, _ := strconv.Atoi(command[1])

		direction := 1

		if command[0] == "L" {
			direction = -1
		}
		newPoint, crossings := turnAndCountZeroCrossings(point, direction, value)
		point = newPoint
		total += crossings
	}

	return strconv.Itoa(total)
}

func turnAndCountZeroCrossings(point int, direction int, amount int) (int, int) {
	crossings := 0

	for amount > 0 {
		point += direction
		amount -= 1

		if point%100 == 0 {
			crossings += 1
		}
	}

	return point, crossings
}

func parseLines(lines []string) [][]string {
	var commands [][]string

	for _, line := range lines {
		command := []string{
			line[0:1],
			line[1:],
		}
		commands = append(commands, command)
	}

	return commands
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "1",
	}

	runner.RunDay(day)
}
