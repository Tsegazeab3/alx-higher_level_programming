#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    my_list.reverse()
    for number in my_list:
        print("{:d}".format(number))


if __name__ == "__main__":
    print_reversed_list_integer()
