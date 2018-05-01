#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if not isinstance(value, int):
            raise ValueError("Exception: Unknown format code\
 'd' for object of type 'str'")
        print("{:d}".format(value))
        return True

    except ValueError as ve:
        print(ve)
        return False
