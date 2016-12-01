#!/usr/bin/env python3

"""Day 1: ."""

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

def north(coords, step):
    """Return new coordinates after moving some steps to the direction."""
    for _ in range(step):
        coords[1] += 1
        if str(coords) in VISITED:
            print("Visited already: {}, dist: {}".format(str(coords), calc_distance(coords)))
        VISITED.append(str(coords))
    return coords

def east(coords, step):
    """Return new coordinates after moving some steps to the direction."""
    for _ in range(step):
        coords[0] += 1
        if str(coords) in VISITED:
            print("Visited already: {}, dist: {}".format(str(coords), calc_distance(coords)))
        VISITED.append(str(coords))
    return coords

def south(coords, step):
    """Return new coordinates after moving some steps to the direction."""
    for _ in range(step):
        coords[1] -= 1
        if str(coords) in VISITED:
            print("Visited already: {}, dist: {}".format(str(coords), calc_distance(coords)))
        VISITED.append(str(coords))
    return coords

def west(coords, step):
    """Return new coordinates after moving some steps to the direction."""
    for _ in range(step):
        coords[0] -= 1
        if str(coords) in VISITED:
            print("Visited already: {}, dist: {}".format(str(coords), calc_distance(coords)))
        VISITED.append(str(coords))
    return coords


FUNCTIONS = [north, east, south, west]
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
        position = FUNCTIONS[heading](position, steps)

    print("Final position: {}, dist: {}".format(str(position), calc_distance(position)))

if __name__ == "__main__":
    main()
