#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == idx:
            new_list[i] = my_list[i + 1]
        else:
            new_list[i] = my_list[i]
    return new_list