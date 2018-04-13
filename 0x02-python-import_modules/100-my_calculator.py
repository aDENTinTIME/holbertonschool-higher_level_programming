#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    total = 0

    if op == "+":
        total = add(a, b)
    elif op == "-":
        total = sub(a, b)
    elif op == "*":
        total = mul(a, b)
    elif op == "/":
        total = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, total))
if __name__ == "__main__":
    main()
