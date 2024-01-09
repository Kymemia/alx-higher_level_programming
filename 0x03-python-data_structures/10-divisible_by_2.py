#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lisy = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            new_lisy.append(True)
        else:
            new_lisy.append(False)
    return new_lisy
