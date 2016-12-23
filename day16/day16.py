#!/usr/bin/env python

"""Day 16: Dragon Checksum."""

INPUT = (272, "11110010111001001")
INPUT = (35651584, "11110010111001001")
# INPUT = (20, "10000")

def extend(data):
    reinverse = data[::-1].translate(str.maketrans('01', '10'))
    return f"{data}0{reinverse}"

def fill_disk(disk_size, data):
    while len(data) < disk_size:
        data = extend(data)
    return data[:disk_size]

def checksum(data):
    pairs = [data[i:i + 2] for i in range(0, len(data), 2)]
    condensed = "".join(["1" if p[0] == p[1] else "0" for p in pairs])
    while len(condensed) % 2 == 0:
        condensed = checksum(condensed)
    return condensed

def main():
    filled = fill_disk(*INPUT)
    print(checksum(filled))

if __name__ == "__main__":
    main()
