#!/usr/bin/python3
"""
Module: Text Indentation.
A function that prints text
with 2 new lines after each
of these characters:
    - '.' character.
    - '?' character.
    - ':' character.
"""


def text_indentation(text):
    """
    Function to print the text after
    the characters {'.', ':', '?'}.

    Arguments:
        - text:
            * Input string for our
            function.
    Returns:
        - No returns for our function.
    Raises:
        - TypeError:
            * If the text generated is
            not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    SEN = text[:]

    for DELIM in ".:?":
        TextLIST = SEN.split(DELIM)
        SEN = ""
        for LINE in TextLIST:
            LINE = LINE.strip(" ")
            SEN = LINE + DELIM if SEN is "" else SEN + "\n\n" + LINE + DELIM
    print(SEN[:-3], end="")
