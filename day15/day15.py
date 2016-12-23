#!/usr/bin/env python

"""Day 15: Timing is Everything."""

from collections import namedtuple

INPUT_FILE = "day15_input.txt"
# INPUT_FILE = "day15x_input.txt"

def main():
    Disc = namedtuple('Disc', ['number', 'positions', 'start_pos'])

    with open(INPUT_FILE, 'r') as input_file:
        instructions = [line.strip() for line in input_file]

    discs = []
    for disc in instructions:
        split = disc.split()
        discs.append(Disc(int(split[1][1]), int(split[3]), int("".join(split[11][:-1]))))
    discs.append(Disc(7, 11, 0))

    button_time = 0
    while not all([True if ((button_time + disc.number) + disc.start_pos) % disc.positions == 0 else False for disc in discs]):
        button_time += 1
    print(button_time)

if __name__ == "__main__":
    main()
