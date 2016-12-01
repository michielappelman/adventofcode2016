#!/usr/bin/env python3

"""Day 1: No Time for a Taxicab."""

import re

INPUT_FILE = "day01_input.txt"

with open(INPUT_FILE, 'r') as f:
    for line in f:
        pattern = r'([LR]\d*)'
        result = re.findall(pattern, line)
        instructions = [[c[0], int(c[1:])] for c in result]

def calc_distance(coords):
    """Calculates the taxicab distance of point on a grid."""
    return abs(coords[0]) + abs(coords[1])

def move(coords, direction, step):
    """Return new coordinates after moving some steps to the direction."""
    for _ in range(step):
        if direction == 0: # North
            coords[1] += 1
        if direction == 1: # East
            coords[0] += 1
        if direction == 2: # South
            coords[1] -= 1
        if direction == 3: # West
            coords[0] -= 1
        if str(coords) in VISITED:
            print("Visited already: {}, dist: {}".format(str(coords), calc_distance(coords)))
        VISITED.append(str(coords))
    return coords

VISITED = []

def main():
    """Main function."""
    heading = 0
    position = [0, 0]

    for i in instructions:
        direction, steps = i
        if direction == "L":
            heading = (heading - 1) % 4
        elif direction == "R":
            heading = (heading + 1) % 4
        position = move(position, heading, steps)

    print("Final position: {}, dist: {}".format(str(position), calc_distance(position)))

if __name__ == "__main__":
    main()
