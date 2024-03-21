#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        copied_list = list(my_string)
        no_cs = copied_list.count('c')
        no_Cs = copied_list.count('C')
        for i in range(no_cs):
            copied_list.remove('c')
        for j in range(no_Cs):
            copied_list.remove('C')
        return(''.join(copied_list))
    else:
        return None


if __name__ == "__main__":
    no_c()
