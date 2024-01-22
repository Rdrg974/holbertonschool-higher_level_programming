#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    if n < 0:
        return str
    for i in range(len(str)):
        if i != n:
            result += str[i]
    return result
