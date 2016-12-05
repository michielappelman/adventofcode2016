#!/usr/bin/env python3

"""Day 5: How About a Nice Game of Chess?"""

from hashlib import md5

INPUT = "abbhdwsy"

def main():
    password = ""
    i = 0
    md5hash = md5()
    md5hash.update(INPUT.encode('utf-8'))
    while len(password) < 8:
        incremental_md5 = md5hash.copy()
        incremental_md5.update(str(i).encode('utf-8'))
        if incremental_md5.hexdigest().startswith("00000"):
            password += incremental_md5.hexdigest()[5]
        i += 1
    print(password)

    password = list("xxxxxxxx")
    i = 0
    while "x" in password:
        incremental_md5 = md5hash.copy()
        incremental_md5.update(str(i).encode('utf-8'))
        if (incremental_md5.hexdigest().startswith("00000") and
                incremental_md5.hexdigest()[5].isdigit() and
                int(incremental_md5.hexdigest()[5]) < 8 and
                password[int(incremental_md5.hexdigest()[5])] == "x"):
            password[int(incremental_md5.hexdigest()[5])] = incremental_md5.hexdigest()[6]
        i += 1
    print("".join(password))

if __name__ == "__main__":
    main()
