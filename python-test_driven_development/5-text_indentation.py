#!/usr/bin/python3
"""This module contains a function
    that prints a text with 2 new lines after.
"""


def text_indentation(text):
    """Print a text with 2 new lines after.

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If text is not a string

    Returns:
        _type_: The text with 2 new lines after
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        if i == " " and len(new_text) == 0:
            continue
        elif i == " " and new_text[-1] in "\n":
            continue
        new_text += i
        if i in ".?:!":
            new_text += "\n\n"
    print(new_text, end="")
