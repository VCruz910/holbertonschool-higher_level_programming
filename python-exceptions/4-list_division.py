#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    DIV = []
    TempResult = 0
    for i in range(0, list_length):
        try:
            TempResult = my_list_1[i] / my_list_2[i]
        except TypeError:
            TempResult = 0
            print("wrong type")
        except ZeroDivisionError:
            TempResult = 0
            print("division by 0")
        except IndexError:
            TempResult = 0
            print("out of range")
        finally:
            pass
        DIV.append(TempResult)
    return (DIV)
