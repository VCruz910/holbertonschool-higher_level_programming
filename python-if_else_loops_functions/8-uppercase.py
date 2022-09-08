#!/usr/bin/python3
def uppercase(str):
    for Char in range(len(str)):
        if ord(str[Char]) >= 97 and ord(str[Char]) <=122:
            Num = 32
        else:
            Num = 0
        print("{:c}".format(ord(str[Char]) - Num), end='')
    print()
