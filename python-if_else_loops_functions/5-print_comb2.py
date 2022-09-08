#!/usr/bin/python3
for Num in range(0, 100):
    if Num != 99:
        print("{:02d}, ".format(Num), end='')
    else:
        print("{:02d}".format(Num))
