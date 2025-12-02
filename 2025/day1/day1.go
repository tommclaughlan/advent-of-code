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

		fullTurns := value / 100
		partTurn := value % 100

		start := point

		total += fullTurns

		if command[0] == "R" {
			point += partTurn
		}
		if command[0] == "L" {
			point -= partTurn
		}
		if point == 0 {
			total += 1
		}
		if point >= 100 {
			if start != 0 {
				total += 1
			}
			point -= 100
		}
		if point < 0 {
			if start != 0 {
				total += 1
			}
			point += 100
		}
	}

	return strconv.Itoa(total)
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
