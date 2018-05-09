#!/usr/bin/python3
"""it would be great if i had a way of accessing the iterator `i` in the
calling program, i could use that as my multiplier
global i"""
def magic_string():
    return "Holberton" + ", Holberton" * 0

vvv passing code vvv

#!/usr/bin/python3
count = 0
def magic_string():
    global count; count += 1; return "Holberton" + ", Holberton" * (count - 1)
