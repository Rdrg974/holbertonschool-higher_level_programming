#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n > 0:
        l_pascal = [[1]]
        for i in range(n - 1):
            my_list = [1]
            if i > 0:
                n = len(l_pascal)
                for j in range(n - 1):
                    my_list.append(l_pascal[i][j] + l_pascal[i][j + 1])
            my_list.append(1)
            l_pascal.append(my_list)
        return l_pascal
    return []
