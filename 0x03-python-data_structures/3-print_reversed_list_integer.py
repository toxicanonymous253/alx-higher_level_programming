#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Check if the list is None
    if my_list is None:
        # If it is, print an empty string
        print('', end='')
    else:
        # Check if the list is empty
        if not my_list:
            # If it is, print an empty string
            print('', end='')
        else:
            # Reverse the list
            my_list.reverse()
            # Print each element of the list in reverse order
            for i in range(len(my_list)):
                print("{:d}".format(my_list[i]))
