#!/usr/bin/python3
def no_c(my_string):
    STRLenght = len(my_string)
    STRNew = my_string[:]
    STR = 0

    for LTR in range(STRLenght):
        if (my_string[LTR] == 'c' or my_string[LTR] == 'C'):
            STRNew = STRNew[:(LTR - STR)] + my_string[(LTR + 1):]
            STR += 1
    return (STRNew)
