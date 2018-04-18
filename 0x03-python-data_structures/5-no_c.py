#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    i = 0
    for c in range(len(new_list)):
        if my_string[c] != ord('c') or my_string[c] != ord('C'):
            new_list[i] = new_list[c]
            i += 1
        else:
            print(c)
    new_string = ''.join(new_list)
    return new_string
