#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    it = 0
    its = 0

    for tup in my_list:
        it += tup[0] * tup[1]
        its += tup[1]

    return (num / den)
