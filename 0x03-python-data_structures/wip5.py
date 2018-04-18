#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    i = 0
    for c in range(len(new_list)):
        if c == ord('c') or c == ord('C'):
            i += 1
            continue
        else:
            new_list[i] = new_list[c]
    new_string = ''.join(new_list)
    return new_string
