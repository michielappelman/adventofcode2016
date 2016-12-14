#!/usr/bin/env python

"""Day 12: Leonardo's Monorail."""

from collections import defaultdict

INPUT_FILE = "day12_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [tuple(line.strip().split()) for line in input_file]
    counter = 0
    registers = defaultdict(int)
    registers['c'] = 1
    while counter < len(instructions):
        instruction = instructions[counter]
        if instruction[0] == 'cpy':
            if instruction[1].isdigit():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]
        elif instruction[0] == 'jnz':
            if instruction[1].isdigit():
                compare = int(instruction[1])
            else:
                compare = registers[instruction[1]]
            if compare != 0:
                counter += (int(instruction[2]) - 1)
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        elif instruction[0] == 'dec':
            registers[instruction[1]] -= 1
        else:
            print("Error parsing", repr(instruction))
        counter += 1
    print(registers)

if __name__ == "__main__":
    main()
