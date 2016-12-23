#!/usr/bin/env python

"""Day 17: Two Steps Forward."""

from hashlib import md5

INPUT = ["ihgpwlah",
         "kglvqrro",
         "ulqzkmiv",
         "qljzarfv"]
MOVEMENT = {0: (0, -1),
            1: (0, 1),
            2: (-1, 0),
            3: (1, 0)}
DESCRIPTION = {0: "U",
               1: "D",
               2: "L",
               3: "R"}

def get_next_moves(passcode, path, curr_loc):
    next_moves = []
    for i, character in enumerate(md5(f"{passcode}{path}".encode()).hexdigest()[:4]):
        if 97 < ord(character) < 103:
            location = tuple([c + n for c, n in zip(curr_loc, MOVEMENT[i])])
            if 0 < location[0] < 5 and 0 < location[1] < 5:
                next_moves.append((path + DESCRIPTION[i], location))
    return next_moves

def find_path(passcode):
    next_moves = []
    next_moves.extend(get_next_moves(passcode, "", (1, 1)))

    while next_moves:
        next_move = next_moves.pop(0)
        path, location = next_move
        if location == (4, 4):
            return path
        next_moves.extend(get_next_moves(passcode, path, location))

def find_longest_path(passcode):
    next_moves = []
    next_moves.extend(get_next_moves(passcode, "", (1, 1)))

    while next_moves:
        path, location = next_moves.pop(0)
        for nm in get_next_moves(passcode, path, location):
            if nm[1] == (4, 4):
                longest = len(path) + 1
            else:
                next_moves.append(nm)
    return longest

def main():
    for passcode in INPUT:
        shortest_path = find_path(passcode)
        longest = find_longest_path(passcode)
        print(f"{passcode} - shortest path: {shortest_path}, longest length: {longest}")

if __name__ == "__main__":
    main()
