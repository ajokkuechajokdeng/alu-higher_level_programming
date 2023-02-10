#!/usr/bin/python3
# 3-print_alphabt.py

"""print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) != 'e' and chr(letter) != 'q':
        print("{:s}".format(chr(letter)), end="")
