package util

import "strings"

type String string

func AsLines(s string) []string {
	lines := strings.Split(s, "\n")
	return lines[0 : len(lines)-1]
}
