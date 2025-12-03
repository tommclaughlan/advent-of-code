package util

import "strings"

func AsLines(s string) []string {
	lines := strings.Split(s, "\n")
	return lines[0 : len(lines)-1]
}
