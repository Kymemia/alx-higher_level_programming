#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    u_sum = 0

    for i in my_list:
        if i not in unique:
            unique.add(i)
            u_sum += i
    return u_sum
