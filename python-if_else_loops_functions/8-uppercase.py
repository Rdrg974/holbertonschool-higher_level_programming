#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        j = ord(char)
        if 97 <= j <= 122:
            result += chr(j - 32)
        else:
            result += char
    print("{}".format(result))
