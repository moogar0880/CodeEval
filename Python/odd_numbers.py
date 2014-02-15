"""Print the odd numbers from 1 to 99.

Print the odd numbers from 1 to 99, one number per line.
"""
from __future__ import print_function
import sys

for x in range(1, 100):
    if x % 2 != 0:
        print(x)
