#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list :
        list_copy = my_list.copy()
        if (idx < 0) or (idx > (len(my_list) - 1)):
            return(list_copy)
        else:
            list_copy[idx] = element
            return(list_copy)
    else:
        return None
