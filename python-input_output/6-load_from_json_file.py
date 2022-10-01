#!/usr/bin/python3
"""Creates an Object from a "JSON file"."""
import json


def load_from_json_file(filename):
    """Returns corresponding Python object."""
    with open(filename, 'r') as f:
        return json.loads(f.read())
