#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        LDigit = number % 10
    else:
        LDigit = number % -10
        LDigit *= -1
    print("{:d}".format(LDigit), end='')
    return (LDigit)
