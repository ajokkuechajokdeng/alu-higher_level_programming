#!/usr/bin/python3
"""
Module that defines a lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return [item for item in dir(obj) if not item.startswith('__')]
