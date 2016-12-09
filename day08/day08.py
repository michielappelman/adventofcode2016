#!/usr/bin/env python3

"""Day 8: Two-Factor Authentication."""

import numpy as np

INPUT_FILE = "day08_input.txt"

class Display:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display_matrix = np.zeros((height, width), dtype=np.bool)

    def __str__(self):
        string_display = ""
        for i, row in enumerate(self.display_matrix):
            for column in row:
                if column:
                    string_display += "#"
                else:
                    string_display += "."
            if i < len(self.display_matrix) - 1:
                string_display += "\n"
        return string_display

    def __repr__(self):
        return "Display({}, {})".format(self.width, self.height)

    def rectangle_on(self, width, height):
        self.display_matrix[:height, :width] = True

    def rotate_column(self, column_index, places):
        self.display_matrix[:, column_index] = np.roll(self.display_matrix[:, column_index], places)

    def rotate_row(self, row_index, places):
        self.display_matrix[row_index, :] = np.roll(self.display_matrix[row_index, :], places)

    def lit(self):
        return np.count_nonzero(self.display_matrix)

def main():
    with open(INPUT_FILE, 'r') as input_file:
        instructions = [line.strip() for line in input_file]
    display = Display(50, 6)
    for instr in instructions:
        if instr.startswith("rect"):
            width = int(instr.split()[1].split('x')[0])
            height = int(instr.split()[1].split('x')[1])
            display.rectangle_on(width, height)
        elif instr.startswith("rotate"):
            direction = instr.split()[1]
            index = int(instr.split()[2][2:])
            places = int(instr.split()[4])
            if direction == "row":
                display.rotate_row(index, places)
            elif direction == "column":
                display.rotate_column(index, places)
            else:
                print("Error matching:", instr)
        else:
            print("Error matching:", instr)
    print(display)
    print(display.lit())

if __name__ == "__main__":
    main()
