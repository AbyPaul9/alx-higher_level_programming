#!/usr/bin/python3
import hidden_4


def main():
    m = dir(hidden_4)
    for i in range(len(m)):
        if(m[i][0] != '_'):
            print("{}".format(m[i]))


if __name__ == "__main__":
    main()
