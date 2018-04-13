#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)
    total = 0

    for i in range(1, argc):
        total += int(argv[i])
    print(total)
if __name__ == "__main__":
    main()
