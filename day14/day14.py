#!/usr/bin/env python

"""Day 14: One-Time Pad."""

from functools import lru_cache
from hashlib import md5
import re

INPUT = "zpqevtbw"

@lru_cache(maxsize=None)
def generate_md5hash(message):
    return md5(message.encode()).hexdigest()

@lru_cache(maxsize=None)
def generate_stretched_md5hash(message):
    hd = md5(message.encode()).hexdigest()
    i = 0
    while i < 2016:
        md5hash = md5()
        md5hash.update(hd.encode())
        hd = md5hash.hexdigest()
        i += 1
    return hd

def single_round(salt):
    i = 0
    keys_found = []
    while len(keys_found) < 64:
        md5hash = generate_md5hash(salt + str(i))
        triplet = re.search(r'(\w)\1\1', md5hash)
        if triplet:
            for j in range(i + 1, i + 1001):
                next_md5hash = generate_md5hash(salt + str(j))
                if triplet.group(0)[0]*5 in next_md5hash:
                    # print(i, md5hash, j, next_md5hash)
                    keys_found.append(i)
        i += 1
    return keys_found[-1]

def stretched_round(salt):
    i = 0
    keys_found = []
    while len(keys_found) < 64:
        md5hash = generate_stretched_md5hash(salt + str(i))
        triplet = re.search(r'(\w)\1\1', md5hash)
        if triplet:
            for j in range(i + 1, i + 1001):
                next_md5hash = generate_stretched_md5hash(salt + str(j))
                if triplet.group(0)[0]*5 in next_md5hash:
                    # print(i, md5hash, j, next_md5hash)
                    keys_found.append(i)
        i += 1
    return keys_found[-1]

def main():
    print(single_round(INPUT))
    print(stretched_round(INPUT))

if __name__ == "__main__":
    main()
