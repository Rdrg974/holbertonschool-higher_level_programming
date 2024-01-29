#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        tmp = my_list[0]
        for i in range(1, len(my_list)):
            if tmp < my_list[i]:
                tmp = my_list[i]
        return tmp
