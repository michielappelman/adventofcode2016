#!/usr/bin/env python3

"""Day 5: How About a Nice Game of Chess?"""

from hashlib import md5
from sys import stdout

INPUT = "abbhdwsy"

def main():
    password_part1 = [None] * 8
    password_part2 = [None] * 8
    i = 0
    found = 0
    while not all(password_part1 + password_part2):
        md5hash = md5()
        md5hash.update(INPUT.encode() + str(i).encode())
        hexdigest = md5hash.hexdigest()

        if hexdigest.startswith("00000"):
            # Tests for Part 1
            if found < 8:
                password_part1[found] = hexdigest[5]
                found += 1
            # Tests for Part 2
            if (hexdigest[5].isdigit() and int(hexdigest[5]) < 8 and
                    password_part2[int(hexdigest[5])] is None):
                password_part2[int(hexdigest[5])] = hexdigest[6]
        # Display BLINKENLIGHTS
        if i % 50000 == 0:
            pw1 = [hexdigest[p] if c is None else c for p, c in enumerate(password_part1)]
            pw2 = [hexdigest[p] if c is None else c for p, c in enumerate(password_part2)]
            msg = "PW1: {} -- PW2: {}\r".format("".join(pw1), "".join(pw2))
            stdout.write(msg)
            stdout.flush()
        i += 1
    # Final Result
    msg = "PW1: {} -- PW2: {}\r".format("".join(password_part1), "".join(password_part2))
    print(msg)

if __name__ == "__main__":
    main()
