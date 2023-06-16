#!/usr/bin/python3
"""
Module 2-my_list
Contains a class MyList that inherits from list
Methods:
    print_sorted(self): Prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
