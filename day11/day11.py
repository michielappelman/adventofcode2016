#!/usr/bin/env python3

"""Day 11: Radioisotope Thermoelectric Generators."""

import re
from itertools import combinations
from collections import defaultdict

INPUT_FILE = "day11_input.txt"
# INPUT_FILE = "day11x_input.txt"

seen = set()

def combine_pairs(floors):
    pair_dict = defaultdict(dict)
    for floor_no, floor in enumerate(floors.values()):
        for content in floor:
            if "microchip" in content:
                pair_dict[content[1]][0] = floor_no
            elif "generator" in content:
                pair_dict[content[1]][1] = floor_no
    pairs = [(m[0], m[1]) for m in pair_dict.values()]
    return sorted(pairs)

def valid_state(floors):
    for floor in floors:
        generators = [elem[1] for elem in floors[floor] if elem[0] == 'generator']
        microchips = [elem[1] for elem in floors[floor] if elem[0] == 'microchip']
        for microchip in microchips:
            if len(generators) > 0 and microchip not in generators:
                return False
    return True

def get_next_moves(current, count, floors):
    moves = []
    move_sets = [[dev] for dev in floors[current]]
    move_sets.extend(combinations(floors[current], 2))

    for delta in (-1, 1):
        new_floor = current + delta
        if new_floor > 3 or new_floor < 0:
            continue

        for combi in move_sets:
            next_floors = dict(floors)
            next_floors[current] = list(set(floors[current]) - set(combi))
            next_floors[new_floor] = list(set(floors[new_floor]) | set(combi))
            if not valid_state(next_floors):
                continue
            move = [new_floor, count+1, next_floors]
            if (new_floor, tuple(combine_pairs(next_floors))) not in seen:
                moves.append(move)
            seen.add((new_floor, tuple(combine_pairs(next_floors))))
    return moves

def search(init, goal):
    next_moves = []
    next_moves.extend(get_next_moves(0, 0, init))

    seen.add((0, tuple(combine_pairs(init))))

    while next_moves:
        next_move = next_moves.pop(0)
        floor, distance, floors = next_move
        if len(floors[3]) == goal:
            return distance
        next_moves.extend(get_next_moves(floor, distance, floors))

def main():
    floors = {}
    with open(INPUT_FILE, 'r') as input_file:
        for line_no, line in enumerate(input_file):
            floor = []
            pattern_gen = r'\s(\w+) generator'
            for material in re.findall(pattern_gen, line):
                floor.append(('generator', material))
            pattern_chip = r'(\w+)-compatible'
            for material in re.findall(pattern_chip, line):
                floor.append(('microchip', material))
            floors[line_no] = floor
    print(search(floors, 10))
    floors[0].extend([('microchip', 'elerium'),
                      ('generator', 'elerium'),
                      ('microchip', 'dilithium'),
                      ('generator', 'dilithium')])
    print(search(floors, 14))

if __name__ == "__main__":
    main()
