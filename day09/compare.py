#!/usr/bin/env python3

import timeit
import re

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

def decode2(line):
    '''
    Decode a line
    Had to move away from regex as it was taking ages
    :return: decoded string
    '''
    #data = list(line)
    data = line
    len_line = 0
    while True:
        # splits the sequence in 2, before the marker and after
        split = data.split(sep='(', maxsplit=1)
        len_line += len(split[0])
        try:
            data = split[1]
            # marker = (<x>x<y>)
            # x is the string before the 'x'
            x, data = data.split(sep='x', maxsplit=1)
            x = int(x)
            # y is the string before the ')'
            y, data = data.split(sep=')', maxsplit=1)
            y = int(y)
            len_line+= y * decode2(data[:x])
            data = data[x:]
        except IndexError:
            # no marker, end of loop
            return len_line

def decompress_markers(line):
    uncompressed_length = 0
    it = re.finditer(r'\(([0-9]+x[0-9]+)\)', line)
    start = 0
    for patt in it:
        if start > patt.start(): # previous iteration went over this marker
            continue
        if start < patt.start():
            uncompressed_length += decompress_markers(line[start:patt.start()]) # /!\ I was skipping this. If the new pattern is further than the previous uncompression length
        numbers = patt.group(1).split('x')
        str_len_to_unc = int(numbers[0])
        times_to_unc = int(numbers[1])

        uncompressed_length += decompress_markers(line[patt.end():patt.end() + str_len_to_unc]) * times_to_unc
        start = patt.end() + str_len_to_unc

    uncompressed_length += len(line[start:]) # add trailing chars in line
    return uncompressed_length

def pilewyll(string):
    decompressed_length = 0
    for line in string:
        decompressed_length += decompress_markers(line)

def main():
    setup_general = """with open("day09_input.txt", 'r') as input_file:
    string = input_file.read().strip()\n"""
    number = 100

    # mappelma
    setup_mappelma = setup_general + "from __main__ import CompressedFile"
    print("mappelma:", timeit.timeit('CompressedFile(string).decompress_length_v2()',
                                     setup=setup_mappelma, number=number))

    # dvanhelm
    setup_dvanhelm = setup_general + "from __main__ import star2"
    print("dvanhelm:", timeit.timeit('star2(string)',
                                     setup=setup_dvanhelm, number=number))

    # rmartini
    setup_rmartini = setup_general + "from __main__ import decode2"
    print("rmartini:", timeit.timeit('decode2(string)',
                                     setup=setup_rmartini, number=number))

    # pilewyll
    setup_pilewyll = setup_general + "from __main__ import decompress_markers\nimport re"
    print("pilewyll:", timeit.timeit('decompress_markers(string)',
                                     setup=setup_pilewyll, number=number))

if __name__ == "__main__":
    main()
