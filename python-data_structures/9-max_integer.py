#!/usr/bin/python3
def max_integer(my_list=[]):
    INTLen = len(my_list)

    if INTLen == 0:
        return (None)

    INTMax = my_list[0]

    for INT in range(1, INTLen):
        if my_list[INT] > INTMax:
            INTMax = my_list[INT]
    return (INTMax)
