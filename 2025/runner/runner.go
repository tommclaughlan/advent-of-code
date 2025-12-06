package runner

import (
	"2025/types"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

func loadSession() string {
	file, err := os.Open(".session")

	if err != nil {
		fmt.Println(".session file not found, please set the session token")
	}

	defer file.Close()

	bytes, err := io.ReadAll(file)

	return string(bytes)
}

func loadInput(day string) string {
	inputDir := "inputs"
	filename := inputDir + "/day" + day + ".txt"

	if content, err := os.ReadFile(filename); err == nil {
		return string(content)
	}

	req, _ := http.NewRequest("GET", "https://adventofcode.com/2025/day/"+day+"/input", nil)

	sessionToken := loadSession()

	req.Header.Add("Cookie", "session="+sessionToken)

	resp, err := http.DefaultClient.Do(req)

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)

	if err != nil {
		panic(err)
	}

	_ = os.MkdirAll(inputDir, 0755)
	_ = os.WriteFile(filename, body, 0644)

	return string(body)
}

func RunDay(day types.Day) {
	input := loadInput(day.Day)

	start := time.Now()
	fmt.Printf("Part 1: %s took %d μs\n", day.Part1(input), time.Since(start).Microseconds())

	start = time.Now()
	fmt.Printf("Part 2: %s took %d μs\n", day.Part2(input), time.Since(start).Microseconds())
}
