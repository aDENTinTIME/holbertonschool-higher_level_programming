#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
full = number
mul = 1
number = str(number)

if number[0] == '-':
    mul = -1

number = int(number[-1])

number *= mul

print("Last digit of {:d} is {:d} ".format(full, number), end="")

if number == 0:
    print("and is 0")
elif number > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
