#!/usr/bin/python3

for y in range(ord("a"), ord("z") + 1):
    if chr(y) != 'q' and chr(y) != 'e':
        print("{}".format(chr(y)), end="")
