#!/usr/bin/python3
"""Writes string to a text file."""


def write_file(filename="", text=""):
    """Writes the file."""
    with open(filename, 'w+') as F:
        return (F.write(text))
