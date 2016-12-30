#!/usr/bin/env python

"""Day 22: Grid Computing."""

import re
from collections import namedtuple
from itertools import permutations

INPUT_FILE = "day22_input.txt"

def main():
    Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'avail', 'in_use'])
    nodes = []

    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            pattern = r'.*/node-x(\d+)-y(\d+)\s+(\d+).\s+(\d+).\s+(\d+).\s+(\d+).*'
            result = re.match(pattern, line)
            nodes.append(Node(*[int(c) for c in result.groups()]))

    viable_pair_count = 0
    for pair in permutations(nodes, 2):
        if pair[0].used != 0 and pair[0].used < pair[1].avail:
            viable_pair_count += 1
    print(viable_pair_count)

if __name__ == "__main__":
    main()
