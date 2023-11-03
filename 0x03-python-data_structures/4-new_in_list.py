#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_size = len(my_list)
    if idx < 0 and idx > list_size:
        return my_list
    # make a copy of original to avoid modifying it
    new_list = my_list[:]
    # replace element at specified index
    new_list[idx] = element
    return new_list
