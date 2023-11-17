#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for key in a_dictionary.keys():
        new_dic[key] = 2 * a_dictionary[key]
    return new_dic
