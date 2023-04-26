#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """prints square with # caharacter"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#"*size, end="")
        print()
