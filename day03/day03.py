#!/usr/bin/env python3

"""Day 3: Squares With Three Sides."""

from itertools import permutations

INPUT_FILE = "day03_input.txt"

def valid_triangle(sides):
    return all([sum(combi[:2]) > combi[2] for combi in permutations(sides)])

def main():
    with open(INPUT_FILE, 'r') as input_file:
        triangles = [[int(side) for side in line.rstrip('\n').split()] for line in input_file]
    print(sum([valid_triangle(triangle) for triangle in triangles]))

if __name__ == "__main__":
    main()
