#!/usr/bin/python3
def element_at(my_list, idx):
    list_xize = len(my_list)

    if idx < 0:
        return None
    if idx > list_xize:
        return None
    return my_list[idx]
