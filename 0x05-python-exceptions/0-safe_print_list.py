#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    y = 0 
    while(y < x):
        try:
            print("{}".format(my_list[y]),end='')
            y = y + 1
        except IndexError:
            break
    print()
    return(y)

    if(__name__ == "__main__"):
        my_list = [1, 2, 3, 4, 5]
        nb_print = safe_print_list(my_list, 2)
        print("nb_print: {:d}".format(nb_print))
        nb_print = safe_print_list(my_list, len(my_list))
        print("nb_print: {:d}".format(nb_print))
        nb_print = safe_print_list(my_list, len(my_list) + 2)
        print("nb_print: {:d}".format(nb_print))
