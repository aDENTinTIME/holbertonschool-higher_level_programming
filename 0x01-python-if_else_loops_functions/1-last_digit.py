#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    last = number % 10
    last *= -1
    number *= -1
else:
    last = number % 10

print("Last digit of {:d} is {:d} ".format(number, last), end="")

if last == 0:
    print("and is 0")
elif last > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
