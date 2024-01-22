#!/usr/bin/python3
i = ord("a")
while i <= ord("z"):
    if i != ord("e") and i != ord("q"):
        print("{}".format(chr(i)), end='')
    i = i + 1
