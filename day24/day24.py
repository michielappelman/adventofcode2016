#!/usr/bin/env python

"""Day 24: Air Duct Spelunking."""

INPUT_FILE = "day24_input.txt"

class AirductMap:
    def __init__(self, description):
        self.width = description.index('\n')
        self.map = description.replace('\n', '')
        self.position = self.map.index('0')

    def __str__(self):
        return self._map_to_string(self.map)

    def __repr__(self):
        return f"{type(self).__name__}('{str(self)}')"

    def __hash__(self):
        return hash(self.map)

    def __eq__(self, other):
        return self.map == other.map

    def _map_to_string(self, airductmap):
        return "\n".join(str(airductmap[start : start + self.width])
                         for start in range(0, len(self.map), self.width))

    @property
    def solved(self):
        return max(self.map) == "0"

    def get_next_moves(self):
        for dest in (self.position - 1, self.position + 1):
            if dest // self.width == self.position // self.width and self.map[dest] != '#':
                yield dest
        for dest in (self.position - self.width, self.position + self.width):
            if 0 <= dest < len(self.map) and self.map[dest] != '#':
                yield dest

    def move(self, dest):
        moved_map = list(self.map)
        moved_map[self.position], moved_map[dest] = ".", "0"
        return AirductMap(self._map_to_string("".join(moved_map)))

class AirductMapBackToPosition(AirductMap):
    def __init__(self, description, to_pos):
        self.width = description.index('\n')
        self.map = description.replace('\n', '')
        self.position = self.map.index('0')
        self.to_pos = to_pos

    @property
    def solved(self):
        return self.map[self.to_pos] == '0' and max(self.map) == "0"

    def move(self, dest):
        moved_map = list(self.map)
        moved_map[self.position], moved_map[dest] = ".", "0"
        return AirductMapBackToPosition(self._map_to_string("".join(moved_map)), self.to_pos)

def shortest_path(start):
    seen = set()
    steps = 0

    next_moves = []
    next_moves.append((0, start))

    while next_moves:
        next_move = next_moves.pop(0)
        steps, grid = next_move
        if grid not in seen:
            if grid.solved:
                return steps
            for destination in grid.get_next_moves():
                next_moves.append((steps + 1, grid.move(destination)))
        seen.add(grid)

def main():
    with open(INPUT_FILE, 'r') as input_file:
        airducts = input_file.read()
    airduct_map = AirductMap(airducts)
    original_pos = airduct_map.position
    steps = shortest_path(airduct_map)
    print("Star 1:", steps)

    steps_back_to_0 = shortest_path(AirductMapBackToPosition(airducts, original_pos))
    print("Star 2:", steps_back_to_0)

if __name__ == "__main__":
    main()
