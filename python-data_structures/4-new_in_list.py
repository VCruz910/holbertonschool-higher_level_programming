#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ELenght = len(my_list)
    New_List = my_list[:]
    if 0 <= idx < ELenght:
        New_List[idx] = element
    return (New_List)
