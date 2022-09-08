#!/usr/bin/python3
for Num in range(0, 90):
    if Num % 10 > Num / 10:
        if Num != 89:
            print("{:02d}, ".format(Num), end='')
        else:
            print("{:02d}".format(Num))
