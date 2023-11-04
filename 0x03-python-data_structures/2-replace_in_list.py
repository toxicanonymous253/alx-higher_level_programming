#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not my_list:
        return my_list
    list_size = len(my_list)
    if idx < 0:
        return my_list
    elif idx > list_size:
        return my_list
    else:
        my_list[idx] = element
        return my_list
