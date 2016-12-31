#!/usr/bin/env python

"""Day 22: Grid Computing."""

import re
from collections import namedtuple
from itertools import permutations

INPUT_FILE = "day22_input.txt"

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'avail', 'in_use'])

class Grid:
    def __init__(self, nodes, goal=(0, 0)):
        self.nodes = sorted(nodes, key=lambda n: (n.y, n.x))
        self.width = max(nodes, key=lambda n: n.x).x + 1
        self.hole = self._find_empty()
        self.goal = self._coord_to_pos(goal)

    def _coord_to_pos(self, coords):
        return coords[0] + coords[1] * self.width

    def _pos_to_coord(self, pos):
        y = pos // self.width
        return (pos - y * self.width, y)

    def solved(self, goal):
        if self.hole == self._coord_to_pos(goal):
            return True
        return False

    @property
    def viable_pairs(self):
        viable_pair_count = 0
        for pair in permutations(self.nodes, 2):
            if pair[0].used != 0 and pair[0].used < pair[1].avail:
                viable_pair_count += 1
        return viable_pair_count

    def __str__(self):
        string_display = ""
        for i, column in enumerate(self.nodes):
            if column.used == 0:
                string_display += "_"
            elif column.in_use > 90:
                string_display += "#"
            else:
                string_display += "."
            if i % self.width == self.width - 1 and i != len(self.nodes) - 1:
                string_display += '\n'
        return string_display

    def _find_empty(self):
        return self.nodes.index(min(self.nodes, key=lambda n: n.used))

    def get_next_moves(self):
        new_poss = []
        for dest in (self.hole - 1, self.hole + 1):  # Left and Right
            if dest // self.width == self.hole // self.width:  # are in same row
                new_poss.append(dest)
        for dest in (self.hole - self.width, self.hole + self.width):  # Up and Down
            if 0 <= dest < len(self.nodes):
                new_poss.append(dest)
        valid_new_poss = []
        for pos in new_poss:
            if self.nodes[pos].used < self.nodes[self.hole].avail:
                valid_new_poss.append(pos)
        yield from valid_new_poss

    def move(self, destination, goal):
        nodes = self.nodes[:]
        nodes[self.hole] = Node(nodes[self.hole].x,
                                nodes[self.hole].y,
                                nodes[self.hole].size,
                                nodes[destination].used,
                                nodes[self.hole].size - nodes[destination].used,
                                int((nodes[destination].used / nodes[self.hole].size) * 100))
        nodes[destination] = Node(nodes[destination].x,
                                  nodes[destination].y,
                                  nodes[destination].size,
                                  0,
                                  nodes[destination].size,
                                  0)
        return Grid(nodes, goal)

def shortest_datapath(start, goal=(0, 0)):
    seen = set()
    steps = 0

    next_moves = []
    next_moves.append((0, start))
    if start.solved(goal):
        return next_moves.pop()

    while next_moves:
        next_move = next_moves.pop(0)
        steps, grid = next_move
        if grid.hole not in seen:
            if grid.solved(goal):
                return steps
            for destination in grid.get_next_moves():
                next_moves.append((steps + 1, grid.move(destination, goal)))
        seen.add(grid.hole)

def main():
    nodes = []

    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            pattern = r'.*/node-x(\d+)-y(\d+)\s+(\d+).\s+(\d+).\s+(\d+).\s+(\d+).*'
            result = re.match(pattern, line)
            nodes.append(Node(*[int(c) for c in result.groups()]))

    grid = Grid(nodes)
    print("Star 1:", grid.viable_pairs)
    steps = shortest_datapath(start=grid, goal=(grid.width - 1, 0))
    print("Star 2:", steps + (5 * (grid.width - 2)))

if __name__ == "__main__":
    main()
