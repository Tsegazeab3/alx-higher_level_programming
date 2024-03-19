#!/usr/bin/python3
# function retrieves an elenment from a list
# idx is the index of the number
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    element_at()
