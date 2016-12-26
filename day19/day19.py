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

if __name__ == "__main__":
    main()
