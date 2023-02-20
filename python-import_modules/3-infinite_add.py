#!/usr/bin/python3

import sys

args = sys.argv[1:]
result = 0

for arg in args:
    result += int(arg)

print(result)
