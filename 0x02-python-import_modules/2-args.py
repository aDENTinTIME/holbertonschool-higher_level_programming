#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
        exit()
    if argc == 2:
        print("1 argument:")
    else:
        print(argc - 1, "arguments:")
    for i in range(1, argc):
        print("{:d}:".format(i), argv[i])
if __name__ == "__main__":
    main()
