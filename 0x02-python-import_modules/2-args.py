#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
        exit()
    print(argc - 1, "arguments:")
    for i in range(1, argc):
        print(argv[i])
if __name__ == "__main__":
    main()
