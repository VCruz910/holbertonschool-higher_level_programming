#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        DIV = a / b
    except (ZeroDivisionError, FloatingPointError):
        DIV = None
    finally:
        print("Inside result: {}".format(DIV))
    return (DIV)
