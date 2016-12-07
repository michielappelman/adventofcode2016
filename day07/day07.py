#!/usr/bin/env python3

"""Day 7: Internet Protocol Version 7."""

from ipv7 import IPv7Address

INPUT_FILE = "day07_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        addresses = [IPv7Address(line.strip()) for line in input_file]
    print(sum([address.supports_tls() for address in addresses]))
    print(sum([address.supports_ssl() for address in addresses]))

if __name__ == "__main__":
    main()
