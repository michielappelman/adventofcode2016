#!/usr/bin/env python3

"""Day 4: Security Through Obscurity."""

import re
from collections import Counter

INPUT_FILE = "day04_input.txt"

def valid_room(room_name, checksum):
    characters = list("".join(room_name))
    counter = Counter(characters)
    most_common = counter.most_common()
    most_common.sort(key=lambda x: x[0])
    most_common.sort(key=lambda x: x[1], reverse=True)
    string_most_common = "".join([c[0] for c in most_common[:5]])
    return string_most_common == checksum

def rotate_alphabet(character, number):
    char_number = ord(character) - 97
    rotated = ((char_number + number) % 26) + 97
    return chr(rotated)

def decrypt_room_name(room_name, sector_id):
    rotated = ["".join([rotate_alphabet(char, sector_id) for char in part]) for part in room_name]
    return "-".join(rotated)

def main():
    rooms = []
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            pattern = r'^(.+)-(\d+)\[(\w+)\]$'
            result = re.match(pattern, line)
            room_name, sector_id, checksum = result.groups()
            room_name = room_name.split('-')
            rooms.append((room_name, int(sector_id), checksum))
    sector_sum = 0
    for room in rooms:
        if valid_room(room[0], room[2]):
            sector_sum += room[1]
            decrypted = decrypt_room_name(room[0], room[1])
            if "north" in decrypted:
                print("Sector ID: ", decrypted, room[1])
    print("Sum: ", sector_sum)

if __name__ == "__main__":
    main()
