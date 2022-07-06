#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    h = len(sys.argv) - 1
    if h == 1:
        print("{:d} argument:".format(h))
    elif h == 0:
        print("{:d} arguments.".format(h))
    else:
        print("{:d} arguments:".format(h))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
