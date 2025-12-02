package main

import (
	"2025/runner"
	"2025/types"
	"strconv"
	"strings"
)

type Range struct {
	start int
	end   int
}

func part1(input string) string {
	ranges := processInput(input)

	invalid := 0

	for _, r := range ranges {
		for i := r.start; i <= r.end; i++ {
			if checkHalves(strconv.Itoa(i)) {
				invalid += i
			}
		}
	}

	return strconv.Itoa(invalid)
}

func part2(input string) string {
	ranges := processInput(input)

	invalid := 0

	for _, r := range ranges {
		for i := r.start; i <= r.end; i++ {
			if checkRepeats(strconv.Itoa(i), 1) {
				invalid += i
			}
		}
	}

	return strconv.Itoa(invalid)
}

func checkHalves(s string) bool {
	length := len(s)
	if length%2 != 0 {
		return false
	}

	first := s[0 : length/2]
	last := s[length/2:]

	return first == last
}

func checkRepeats(s string, length int) bool {
	if len(s)/2 < length {
		return false
	}

	chunks := chunkString(s, length)

	for _, chunk := range chunks {
		if chunks[0] != chunk {
			return checkRepeats(s, length+1)
		}
	}

	return true
}

func chunkString(s string, chunkSize int) []string {
	i := 0
	j := chunkSize
	var chunks []string
	for j <= len(s) {
		chunks = append(chunks, s[i:j])
		i += chunkSize
		j += chunkSize
	}
	if i < len(s) {
		chunks = append(chunks, s[i:])
	}
	return chunks
}

func processInput(input string) []Range {
	ranges := strings.Split(strings.Trim(input, "\n"), ",")

	var result []Range

	for _, r := range ranges {
		temp := strings.Split(r, "-")

		start, _ := strconv.Atoi(temp[0])
		end, _ := strconv.Atoi(temp[1])

		result = append(result, Range{
			start: start,
			end:   end,
		})
	}

	return result
}

func main() {
	day := types.Day{
		Part1: part1,
		Part2: part2,
		Day:   "2",
	}

	runner.RunDay(day)
}
