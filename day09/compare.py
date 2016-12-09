#!/usr/bin/env python3

import time

"""Day 9: Explosives in Cyberspace."""

INPUT_FILE = "day09_input.txt"

class CompressedFile:
    def __init__(self, file_string):
        self.file_string = file_string
        self.compressed_length = len(self.file_string)
        self.decompressed_length = 0

    def __str__(self):
        return self.file_string

    def __repr__(self):
        return "CompressedFile('{}')".format(self)

    def decompress_length_v2(self, string=None):
        length = 0
        # When no string is specified, take this objects own string."
        if string is None:
            string = self.file_string

        # Try to find a bracket ...
        first_bracket = string.find('(')
        # ... when the bracket is not at the first place of the string, the
        # first couple of characters up until the bracket should be counted
        # to the length. And ...
        if first_bracket > 0:
            length += first_bracket

        # ... if there's no bracket, there's nothing to be done, so
        # return the length.
        if first_bracket == -1:
            return len(string)

        # Find the next bracket as well and determine the instructions.
        next_bracket = string.find(')', first_bracket)
        instruction = string[first_bracket + 1:next_bracket]
        no_chars, times = [int(c) for c in instruction.split('x')]

        # With those instructions, find character-set that we need to look at.
        characters = string[next_bracket + 1:next_bracket + 1 + no_chars]

        # Decompress this character-set as well and multiply the result by the
        # number of times we should repeat the set. Add to the length.
        length += self.decompress_length_v2(characters) * times

        # Then there's also a part after the matched character-set, which
        # we'll also have to decompress and then add to the length.
        next_part = string[next_bracket + 1 + no_chars:]
        length += self.decompress_length_v2(next_part)
        return length

def star2(data):
    in_data = list(data)
    data_length = 0
    while len(in_data) != 0:
        char = in_data.pop(0)
        if char != "(":
            data_length = data_length + 1
        else:
            marker = []
            rep_sec = []
            while in_data[0] != ")":
                marker.append(in_data.pop(0))
            in_data.pop(0)
            a, b = ''.join(marker).split('x')
            for _ in range(0, int(a)):
                rep_sec.append(in_data.pop(0))
            data_length = data_length + (star2(rep_sec) * int(b))
    return data_length

def main():
    with open(INPUT_FILE, 'r') as input_file:
        compressed_files = [line.strip() for line in input_file]
    string = compressed_files[0]

    # mappelma
    time_a1 = time.time()
    mappelma = CompressedFile(string)
    length_a = mappelma.decompress_length_v2()
    time_a2 = time.time()
    print("mappelma: {} in {:0.3f} ms".format(length_a, (time_a2-time_a1)*1000.0))

    # dvanhelm
    time_d1 = time.time()
    length_d = star2(string)
    time_d2 = time.time()
    print("dvanhelm: {} in {:0.3f} ms".format(length_d, (time_d2-time_d1)*1000.0))

if __name__ == "__main__":
    main()
