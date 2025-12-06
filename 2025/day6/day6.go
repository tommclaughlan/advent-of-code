package main

import (
	"2025/runner"
	"2025/types"
	"2025/util"
	"strconv"
	"strings"
)

type sum struct {
	numbers []int
	reducer func(nums []int) int
}

func part1(input string) string {
	sums := parseInput(input)
	total := 0
	for _, s := range sums {
		total += s.reducer(s.numbers)
	}

	return strconv.Itoa(total)
}

func part2(input string) string {
	sums := parseInputPart2(input)
	total := 0
	for _, s := range sums {
		total += s.reducer(s.numbers)
	}

	return strconv.Itoa(total)
}

func parseInput(input string) []sum {
	rows := util.AsLines(input)
	nRows := len(rows)

	nSums := len(strings.Fields(rows[0]))

	sums := make([]sum, nSums)
	for s := range sums {
		sums[s] = sum{make([]int, nRows-1), nil}
	}

	for i, row := range rows {
		items := strings.Fields(row)

		for j, item := range items {
			if i == nRows-1 {
				if item == "+" {
					sums[j].reducer = sumFunc
				}
				if item == "*" {
					sums[j].reducer = multFunc
				}
				continue
			}
			val, _ := strconv.Atoi(item)
			sums[j].numbers[i] = val
		}
	}
	return sums
}

func parseInputPart2(input string) []sum {
	rows := util.AsLines(input)
	nRows := len(rows)

	operations := strings.Fields(rows[nRows-1])

	sums := make([]sum, len(operations))
	for s := range sums {
		reducer := multFunc
		if operations[s] == "+" {
			reducer = sumFunc
		}
		sums[s] = sum{make([]int, nRows-1), reducer}
	}

	sumI := 0
	var nums []int
	for i := range len(rows[0]) {
		col := ""
		for j := range nRows - 1 {
			if string(rows[j][i]) != " " {
				col += string(rows[j][i])
			}
		}
		if len(col) == 0 {
			sums[sumI].numbers = nums
			sumI += 1
			nums = nil
		} else {
			number, _ := strconv.Atoi(col)
			nums = append(nums, number)
		}
	}
	sums[sumI].numbers = nums

	return sums
}

func sumFunc(input []int) int {
	total := 0
	for _, num := range input {
		total += num
	}
	return total
}

func multFunc(input []int) int {
	result := 1
	for _, num := range input {
		result *= num
	}
	return result
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "6",
	}

	runner.RunDay(day)
}
