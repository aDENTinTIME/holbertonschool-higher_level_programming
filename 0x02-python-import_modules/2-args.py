#!/usr/bin/python3
from sys import argv


argc = len(argv)

if argc == 1:
    print("0 arguments.")
    exit()

print(argc - 1, "arguments:")
for i in range(1, argc):
    print(argv[i])

