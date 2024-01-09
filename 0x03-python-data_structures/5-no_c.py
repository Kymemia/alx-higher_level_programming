#!/usr/bin/python3
def no_c(my_string):
    ondoa = set('cC')
    new_string = ''.join(char for char in my_string if char not in ondoa)
    return new_string
