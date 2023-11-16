#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list) #set() eliminates duplicates
    return sum(unique_numbers)
