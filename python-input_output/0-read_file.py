#!/usr/bin/python3
"""Reads file and prints it in STDOUT."""


def read_file(filename=""):
    """Reads the file."""
    with open(filename, 'r', encoding="utf-8") as F:
        ReadTXT = F.read()
        print(ReadTXT, end="")
