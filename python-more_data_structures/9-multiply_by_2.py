#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    NewDIR = a_dictionary.copy()
    KeyList = list(NewDIR.keys())

    for DIC in KeyList:
        NewDIR[DIC] *= 2

    return (NewDIR)
