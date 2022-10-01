#!/usr/bin/python3
"""Appends a string at end of text file."""


def append_write(filename="", text=""):
    """Appends a string."""
    with open(filename, 'a+') as F:
        return (F.write(text))
