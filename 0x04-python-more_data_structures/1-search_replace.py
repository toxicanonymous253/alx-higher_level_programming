#!/usr/bin/python3
def search_replace(my_list, search, replace):
    duplicated_list = list(my_list)
    index_to_replace = duplicated_list.index(search)
    duplicated_list[index_to_replace] = replace
    return duplicated_list
