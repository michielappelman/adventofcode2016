#!/usr/bin/env python

"""Day 13: A Maze of Twisty Little Cubicles."""

seen = set()

def is_wall(x, y, song):
    calculate = (x*x + 3*x + 2*x*y + y + y*y) + song
    binary_list = [int(b) for b in list(format(calculate, 'b'))]
    return sum(binary_list) % 2 == 1

def get_next_moves(x, y, song, distance):
    moves = []
    ways = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
    for way in ways:
        if way[0] < 0 or way[1] < 0:
            continue
        if is_wall(*way, song):
            continue
        move = (*way, distance + 1)
        if move not in seen:
            moves.append(move)
        seen.add(move)
    return moves

def search(song, goal):
    next_moves = []
    next_moves.extend(get_next_moves(1, 1, song, 0))

    seen.add((1, 1, 0))

    while next_moves:
        next_move = next_moves.pop(0)
        print(next_move)
        x, y, distance = next_move
        if [x, y] == goal:
            return distance
        next_moves.extend(get_next_moves(x, y, song, distance))

def main():
    # print(search(10, [7, 4]))
    print(search(1364, [31, 39]))

if __name__ == "__main__":
    main()
