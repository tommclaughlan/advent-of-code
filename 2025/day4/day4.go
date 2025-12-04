package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"strconv"
)

func part1(input string) string {
	rows := util.AsLines(input)

	total := 0

	for i, line := range rows {
		for j := range line {

			cell := string(rows[i][j])
			if cell == "@" && countAdjacents(rows, i, j, "@") < 4 {
				total += 1
			}
		}
	}

	return strconv.Itoa(total)
}

func part2(input string) string {
	rows := util.AsLines(input)

	prevTotal := -1
	total := 0
	var removed [][]int

	for total != prevTotal {
		prevTotal = total
		for i, line := range rows {
			for j := range line {

				cell := string(rows[i][j])
				if cell == "@" && countAdjacents(rows, i, j, "@") < 4 {
					total += 1
					removed = append(removed, []int{i, j})
				}
			}
		}

		for _, coords := range removed {
			i := coords[0]
			j := coords[1]
			rows[i] = replaceChar(rows[i], '.', j)
		}
	}

	return strconv.Itoa(total)
}

func replaceChar(s string, r rune, i int) string {
	out := []rune(s)
	out[i] = r
	return string(out)
}

func countAdjacents(grid []string, row int, col int, char string) int {
	total := 0
	for i := row - 1; i <= row+1; i++ {
		for j := col - 1; j <= col+1; j++ {
			if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) || (row == i && col == j) {
				continue
			}
			cell := string(grid[i][j])

			if cell == char {
				total++
			}
		}
	}
	return total
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "4",
	}

	runner.RunDay(day)
}
