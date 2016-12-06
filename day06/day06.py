#!/usr/bin/env python3

"""Day 6: Signals and Noise."""

from collections import Counter
import numpy as np

INPUT_FILE = "day06_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [[c for c in line.strip()] for line in input_file]
    array = np.array(instructions)
    transposed = array.transpose()
    message = ""
    for column in transposed:
        most_common = Counter("".join(column)).most_common(1)
        message += most_common[0][0]
    print(message)

if __name__ == "__main__":
    main()
