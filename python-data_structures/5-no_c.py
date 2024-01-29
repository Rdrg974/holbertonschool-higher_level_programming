#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_list += ch
    return new_list
