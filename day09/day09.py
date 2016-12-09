#!/usr/bin/env python3

"""Day 9: Explosives in Cyberspace."""

INPUT_FILE = "day09_input.txt"
# INPUT_FILE = "day09x_input.txt"

class CompressedFile:
    def __init__(self, file_string):
        self.file_string = file_string
        self.compressed_length = len(self.file_string)
        self.decompressed_length = 0

    def __str__(self):
        return self.file_string

    def __repr__(self):
        return "CompressedFile('{}')".format(self)

    def decompress(self, string=None):
        decompressed_string = ""
        if string is None:
            string = self.file_string
        first_bracket = string.find('(')
        if first_bracket > 0:
            decompressed_string += string[0:first_bracket]
        if first_bracket == -1:
            return string
        next_bracket = string.find(')', first_bracket)
        instruction = string[first_bracket + 1:next_bracket]
        no_chars, times = [int(c) for c in instruction.split('x')]
        characters = string[next_bracket + 1:next_bracket + 1 + no_chars]
        decompressed_string += characters * times
        next_part = string[next_bracket + 1 + no_chars:]
        decompressed_string += self.decompress(next_part)
        return decompressed_string

    def decompress_v2(self, string=None):
        decompressed_string = ""
        if string is None:
            string = self.file_string
        first_bracket = string.find('(')
        if first_bracket > 0:
            decompressed_string += string[0:first_bracket]
        if first_bracket == -1:
            return string
        next_bracket = string.find(')', first_bracket)
        instruction = string[first_bracket + 1:next_bracket]
        no_chars, times = [int(c) for c in instruction.split('x')]
        characters = string[next_bracket + 1:next_bracket + 1 + no_chars]
        decompressed_string += self.decompress_v2(characters) * times
        next_part = string[next_bracket + 1 + no_chars:]
        decompressed_string += self.decompress_v2(next_part)
        return decompressed_string

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

def main():
    with open(INPUT_FILE, 'r') as input_file:
        compressed_files = [CompressedFile(line.strip()) for line in input_file]
    for compressed_file in compressed_files:
        # print(len(compressed_file.decompress()))
        # print(len(compressed_file.decompress_v2()))
        print(compressed_file.decompress_length_v2())

if __name__ == "__main__":
    main()
