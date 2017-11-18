package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"

	"github.com/michielappelman/adventofcode2016/generic"
)

const (
	N = iota
	E
	S
	W
)

type position struct {
	heading int
	x       int
	y       int
}

func (p *position) move(instruction string) {
	turn := string(instruction[0])
	steps, _ := strconv.Atoi(instruction[1:len(instruction)])
	switch turn {
	case "L":
		if p.heading == 0 {
			p.heading = 3
			break
		}
		p.heading = (p.heading - 1) % 4
	case "R":
		p.heading = (p.heading + 1) % 4
	}
	switch p.heading {
	case N:
		p.y += steps
	case S:
		p.y -= steps
	case E:
		p.x += steps
	case W:
		p.x -= steps
	}
}

func main() {
	args := os.Args
	if len(args) < 2 {
		log.Fatal("Input filename not given...")
	}

	input_lines := generic.LoadLines(args[1])
	instructions := generic.SplitLine(input_lines[0], ", ")

	currentPosition := &position{heading: 0, x: 0, y: 0}

	for _, instruction := range instructions {
		currentPosition.move(instruction)
	}
	dist := math.Abs(float64(currentPosition.x)) + math.Abs(float64(currentPosition.y))
	fmt.Println("Absolute distance:", dist)
}
