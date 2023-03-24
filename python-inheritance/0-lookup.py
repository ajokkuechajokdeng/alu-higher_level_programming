#!/usr/bin/python3
"""
Module that defines a lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return [item for item in dir(obj) if not item.startswith('__')]
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
