#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    array = dir(hidden)
    for i in range(len(array)):
        if array[i][0] != "_":
            print("{}".format(array[i]))
