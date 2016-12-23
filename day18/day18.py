#!/usr/bin/env python

"""Day 18: Like a Rogue."""

from itertools import chain

INPUT = "..^^."
INPUT = ".^^.^.^^^^"
INPUT = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

class Floor:
    def __init__(self, first_row):
        self.rows = []
        self.rows.append([True if c == "." else False for c in first_row])

    def __str__(self):
        string_display = ""
        for i, row in enumerate(self.rows):
            for column in row:
                if column:
                    string_display += "."
                else:
                    string_display += "^"
            if i < len(self.rows) - 1:
                string_display += "\n"
        return string_display

    def _add_row(self):
        old = self.rows[-1]
        new = []
        for i, _ in enumerate(old):
            if i == 0:
                l = True
            else:
                l = old[i-1]
            c = old[i]
            try:
                r = old[i+1]
            except IndexError:
                r = True
            if not l and not c and r:
                new.append(False)
            elif l and not c and not r:
                new.append(False)
            elif not l and c and r:
                new.append(False)
            elif l and c and not r:
                new.append(False)
            else:
                new.append(True)
        self.rows.append(new)

    def fill_floor(self, rows):
        while len(self.rows) < rows:
            self._add_row()

    def count_safe_tiles(self):
        return sum(chain.from_iterable(self.rows))

def main():
    floor = Floor(INPUT)
    floor.fill_floor(rows=400000)
    # print(floor)
    print(floor.count_safe_tiles())

if __name__ == "__main__":
    main()
