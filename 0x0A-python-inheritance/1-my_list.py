#!/usr/bin/python3
"""definition of class, My list, that inherits from list"""


class MyList(list):
    """class definition"""
    def print_sorted(self):
        """prints list, but sorted (ascending sort)"""
        print(sorted(self))
