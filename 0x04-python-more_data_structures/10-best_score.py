#!/usr/bin/python3
def best_score(a_dictionary):
    point = ""
    my_list = list(a_dictionary.keys())
    for i in my_list:
        if a_dictionary[i] > point[i]:
            point = i
    return point
