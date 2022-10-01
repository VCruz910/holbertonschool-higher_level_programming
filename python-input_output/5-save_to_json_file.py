#!/usr/bin/python3
"""Writes an Object to text file, using JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """Sends JSON representation to file."""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
