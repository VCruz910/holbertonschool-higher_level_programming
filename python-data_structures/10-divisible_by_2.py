#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    DIVCheck = []

    for INT in range(len(my_list)):
        if my_list[INT] % 2 == 0:
            DIVCheck.append(True)
        else:
            DIVCheck.append(False)
    return (DIVCheck)
