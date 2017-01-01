#!/usr/bin/env python

"""Day 23: Safe Cracking."""

from collections import defaultdict

INPUT_FILE = "day23_input.txt"

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [line.strip().split() for line in input_file]
    counter = 0
    registers = defaultdict(int)
    registers['a'] = 7
    while counter < len(instructions):
        instruction = instructions[counter]
        if instruction[0] == 'tgl':
            try:
                tgl_instr = int(instruction[1])
            except ValueError:
                tgl_instr = registers[instruction[1]]
            tgl_counter = counter + tgl_instr
            try:
                tgl_instr = instructions[tgl_counter]
            except IndexError:
                counter += 1
                continue
            if len(tgl_instr) == 2:
                if tgl_instr[0] == 'inc':
                    tgl_instr[0] = 'dec'
                else:
                    tgl_instr[0] = 'inc'
            if len(tgl_instr) == 3:
                if tgl_instr[0] == 'jnz':
                    tgl_instr[0] = 'cpy'
                else:
                    tgl_instr[0] = 'jnz'
        elif instruction[0] == 'cpy':
            try:
                first = int(instruction[1])
            except ValueError:
                first = registers[instruction[1]]
            if instruction[2].isdigit():
                counter += 1
                continue
            registers[instruction[2]] = first
        elif instruction[0] == 'jnz':
            try:
                compare1 = int(instruction[1])
            except ValueError:
                compare1 = registers[instruction[1]]
            try:
                compare2 = int(instruction[2])
            except ValueError:
                compare2 = registers[instruction[2]]
            if compare1 != 0:
                counter += (compare2 - 1)
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        elif instruction[0] == 'dec':
            registers[instruction[1]] -= 1
        else:
            print("Error parsing", repr(instruction))
        counter += 1
    print(registers['a'])

if __name__ == "__main__":
    main()
