#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ListORD= list(a_dictionary.keys())
    ListORD.sort()
    for KEYS in ListORD:
        print("{}: {}".format(KEYS, a_dictionary.get(KEYS)))
