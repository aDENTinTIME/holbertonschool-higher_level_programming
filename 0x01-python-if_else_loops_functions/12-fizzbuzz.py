#!/usr/bin/python3

for i in range(1, 101):
    if not (i % 3) and not (i % 5):
        print('FizzBuzz', end=' ')
    elif not (i % 3):
        print('Fizz', end=' ')
    elif not (i % 5):
        print('Buzz', end=' ')
    else:
        print(i, end=' ')
print()
