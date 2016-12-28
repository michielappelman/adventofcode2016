#!/usr/bin/env python

"""Day 20: Firewall Rules."""

INPUT_FILE = "day20_input.txt"
# INPUT_FILE = "day20x_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [line.strip().split('-') for line in input_file]
    ranges = [(int(low), int(high)) for low, high in instructions]
    ranges.sort(key=lambda x: x[0])

    ip_address = 0
    i = 0
    allowed = []
    while ip_address < 4294967296:
        low, high = ranges[i]
        if ip_address >= low:
            if ip_address <= high:
                ip_address = high + 1
            else:
                i += 1
        else:
            allowed.append(ip_address)
            ip_address += 1
    print(allowed[0])
    print(len(allowed))

if __name__ == "__main__":
    main()
