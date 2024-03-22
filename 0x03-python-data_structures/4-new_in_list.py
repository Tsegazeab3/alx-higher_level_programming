#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if 0 <= idx < len(my_list):
        list_copy = my_list[:]
        list_copy[idx] = element
        return(list_copy)
    return my_list
