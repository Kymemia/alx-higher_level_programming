#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return 'None'
    else:
        max = my_list[0]
        for x in range(len(my_list)):
            if my_list[x] > max:
                max = my_list[x]
        return max
