#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
