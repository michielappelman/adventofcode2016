#!/usr/bin/env python

"""Day 14: One-Time Pad."""

from functools import lru_cache
from hashlib import md5
import re

INPUT = "zpqevtbw"
# INPUT = "abc"

@lru_cache(maxsize=None)
def generate_md5hash(message):
    md5hash = md5()
    md5hash.update(message.encode())
    return md5hash.hexdigest()

def main():
    i = 0
    keys_found = []
    while len(keys_found) < 64:
        md5hash = generate_md5hash(INPUT + str(i))
        triplet = re.search(r'(\w)\1\1', md5hash)
        if triplet:
            for j in range(i + 1, i + 1001):
                next_md5hash = generate_md5hash(INPUT + str(j))
                if triplet.group(0)[0]*5 in next_md5hash:
                    print(i, md5hash, j, next_md5hash)
                    keys_found.append(i)
        i += 1
    print(keys_found[-1])

if __name__ == "__main__":
    main()
