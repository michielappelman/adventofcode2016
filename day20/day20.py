#!/usr/bin/env python

"""Day 20: Firewall Rules."""

INPUT_FILE = "day20_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [line.strip().split('-') for line in input_file]
    ranges = [(int(low), int(high)) for low, high in instructions]
    ranges = sorted(ranges, key=lambda x: x[0])
    ranges.append((4294967296, 4294967296))

    for i, (_, high) in enumerate(ranges):
        try:
            if high + 1 < ranges[i + 1][0]:
                print(high + 1)
        except:
            pass

if __name__ == "__main__":
    main()
