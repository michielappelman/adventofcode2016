#!/usr/bin/env python3

"""Day 6: Signals and Noise."""

from collections import Counter

INPUT_FILE = "day06_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [[c for c in line.strip()] for line in input_file]
    message_part1 = ""
    message_part2 = ""
    for column in zip(*instructions):
        counter = Counter("".join(column)).most_common()
        message_part1 += counter[0][0]
        message_part2 += counter[-1][0]
    print(message_part1, message_part2)

if __name__ == "__main__":
    main()
