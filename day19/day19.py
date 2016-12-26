#!/usr/bin/env python

"""Day 19: An Elephant Named Joseph."""

from collections import deque

INPUT = 3001330

def main():
    ring = deque(i for i in range(1, INPUT + 1))
    while len(ring) > 1:
        ring.rotate(-1)
        ring.popleft()
    print(ring[0])

    ring2 = deque(i for i in range(1, INPUT + 1))
    while len(ring2) > 1:
        half_ring = int(len(ring2) / 2)
        ring2.rotate(-half_ring)
        ring2.popleft()
        ring2.rotate(half_ring - 1)
    print(ring2[0])

if __name__ == "__main__":
    main()
