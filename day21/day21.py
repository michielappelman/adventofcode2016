#!/usr/bin/env python

"""Day 21: Scrambled Letters and Hash."""

from collections import deque

INPUT = ("abcdefgh", "day21_input.txt")
# INPUT = ("abcde", "day21x_input.txt")

def scrambler(plain, instructions):
    def reverse(text, instruction):
        from_pos = int(instruction[1])
        to_pos = int(instruction[3])
        return text[:from_pos] + text[from_pos:to_pos+1][::-1] + text[to_pos+1:]

    def rotate(text, instruction):
        if instruction[0] == "based":
            rotate = text.index(instruction[5])
            if rotate >= 4:
                rotate += 1
            rotate += 1
        else:
            rotate = int(instruction[1])
        neg = 1
        if instruction[0] == "left":
            neg = -1
        ring = deque(text)
        ring.rotate(rotate * neg)
        return "".join(list(ring))

    def move(text, instruction):
        text = list(text)
        popped = text.pop(int(instruction[1]))
        text.insert(int(instruction[4]), popped)
        return "".join(text)

    def swap(text, instruction):
        if instruction[0] == "position":
            from_pos = int(instruction[1])
            to_pos = int(instruction[4])
            text = list(text)
            text[from_pos], text[to_pos] = text[to_pos], text[from_pos]
            return "".join(text)
        elif instruction[0] == "letter":
            return text.translate(str.maketrans(instruction[1] + instruction[4],
                                                instruction[4] + instruction[1]))
        else:
            return None

    instructions = [instr.split() for instr in instructions]
    for instr in instructions:
        plain = locals()[instr[0]](plain, instr[1:])
    return plain

def main():
    with open(INPUT[1], 'r') as input_file:
        instructions = [line.strip() for line in input_file]
    print(scrambler(INPUT[0], instructions))

if __name__ == "__main__":
    main()
