#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    LEN_A = len(tuple_a)
    LEN_B = len(tuple_b)

    if LEN_A == 0:
        A1 = 0
        A2 = 0
    elif LEN_A == 1:
        A1 = tuple_a[0]
        A2 = 0
    else:
        A1 = tuple_a[0]
        A2 = tuple_a[1]

    if LEN_B == 0:
        B1 = 0
        B2 = 0
    elif LEN_B == 1:
        B1 = tuple_b[0]
        B2 = 0
    else:
        B1 = tuple_b[0]
        B2 = tuple_b[1]

    new_tuple = (A1 + B1, A2 + B2)
    return (new_tuple)
