#!/usr/bin/python3
count = 0
def magic_string():
    global count; count += 1; return "Holberton" + ", Holberton" * (count - 1)
