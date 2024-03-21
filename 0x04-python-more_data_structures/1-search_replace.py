#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list1 = []
    for element in my_list:
        if element == search:
            list1.append(replace)
        else:
            list1.append(element)
    return list1
