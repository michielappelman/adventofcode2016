#!/usr/bin/env python3

"""Day 2: Bathroom Security."""

INPUT_FILE = "day02_input.txt"
KEYPAD = """\
1 2 3
4 5 6
7 8 9"""

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
            self.keypad.append([int(num) for num in line.split()])

    def __repr__(self):
        composed = ""
        for i, row in enumerate(self.keypad):
            for num in row:
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

    def button_from_instructions(self, instructions, start=5):
        """Takes a set of instructions and a optional starting number and
        finds the resulting button."""
        row, col = self._button_to_position(start)
        for instruction in instructions:
            if instruction == 'L' and col > 0:
                col -= 1
            elif instruction == 'R' and col < len(self.keypad[0]) -1:
                col += 1
            elif instruction == 'U' and row > 0:
                row -= 1
            elif instruction == 'D' and row < len(self.keypad) -1:
                row += 1
        return self._position_to_button([row, col])

def main():
    """Main function."""
    with open(INPUT_FILE, 'r') as f:
        instructions = [line.strip() for line in f]
    keypad = Keypad(KEYPAD)
    start = 5
    combination = ""
    for line in instructions:
        new = keypad.button_from_instructions(line, start=start)
        combination += str(new)
        start = new
    print(combination)

if __name__ == "__main__":
    main()
