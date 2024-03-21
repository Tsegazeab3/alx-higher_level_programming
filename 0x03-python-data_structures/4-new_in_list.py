#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        list_copy = my_list.copy()
        if idx < 0:
            return(list_copy)
        elif idx > (len(my_list) - 1):
            return(list_copy)
        else:
            list_copy[idx] = element
            return(list_copy)
    else:
        return(None)


if __name__ is "__main__":
    new_in_list()
