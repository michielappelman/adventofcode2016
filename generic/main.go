package generic

import (
	"bufio"
	"log"
	"os"
	"strings"
)

// Splits a string using a certain delimiter, returns slice of strings.
func SplitLine(line string, delim string) []string {
	return strings.Split(line, ", ")
}

// Takes a filename and returns a slice of strings of its lines.
func LoadLines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal("Error reading file", filename, err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return lines
}
