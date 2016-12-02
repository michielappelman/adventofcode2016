#!/usr/bin/env python3

"""Day 2: Bathroom Security."""

INPUT_FILE = "day02_input.txt"
KEYPAD1 = """\
1 2 3
4 5 6
7 8 9"""
KEYPAD2 = """\
x x 1 x x
x 2 3 4 x
5 6 7 8 9
x A B C x
x x D x x"""

class ButtonNotFound(Exception):
    """Raised when a button is not on the keypad."""
    pass

class Keypad:
    """Keypad class loaded with multi-line definition such as
    1 2 3
    4 5 6
    7 8 9
    """
    def __init__(self, keypad_definition):
        self.keypad = []
        for line in keypad_definition.split('\n'):
            self.keypad.append([num if num != "x" else None for num in line.split()])

    def __repr__(self):
        composed = ""
        for i, row in enumerate(self.keypad):
            for num in row:
                if num is None:
                    composed += "  "
                else:
                    composed += "{} ".format(num)
            if i != len(self.keypad) - 1:
                composed += "\n"
        return composed

    def _button_to_position(self, button):
        point = []
        for i, row in enumerate(self.keypad):
            for j, num in enumerate(row):
                if num == button:
                    point = [i, j]
        if not point:
            raise ButtonNotFound(button)
        return point

    def _position_to_button(self, point):
        try:
            return self.keypad[point[0]][point[1]]
        except IndexError:
            return None

    def button_from_instructions(self, instructions, start="5"):
        """Takes a set of instructions and a optional starting number and
        finds the resulting button."""
        row, col = self._button_to_position(start)
        for instruction in instructions:
            if (instruction == 'L' and col > 0
                    and self._position_to_button([row, col-1]) is not None):
                col -= 1
            elif (instruction == 'R' and col < len(self.keypad[0]) - 1
                  and self._position_to_button([row, col+1]) is not None):
                col += 1
            elif (instruction == 'U' and row > 0
                  and self._position_to_button([row-1, col]) is not None):
                row -= 1
            elif (instruction == 'D' and row < len(self.keypad) -1
                  and self._position_to_button([row+1, col]) is not None):
                row += 1
        return self._position_to_button([row, col])

def main():
    """Main function."""
    keypads = [Keypad(KEYPAD1), Keypad(KEYPAD2)]

    with open(INPUT_FILE, 'r') as f:
        instructions = [line.strip() for line in f]

    for keypad in keypads:
        start = "5"
        combination = ""
        for line in instructions:
            new = keypad.button_from_instructions(line, start=start)
            combination += new
            start = new
        print(combination)

if __name__ == "__main__":
    main()
