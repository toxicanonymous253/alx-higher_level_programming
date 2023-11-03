#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list)
    for i in range(list_size, 0, -1):
        print("{}".format(i))
