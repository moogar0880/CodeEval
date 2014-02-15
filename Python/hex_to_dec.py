"""Print the odd numbers from 1 to 99.

Print the odd numbers from 1 to 99, one number per line.
"""
from __future__ import print_function
import sys

for line in open(sys.argv[1], 'r'):
    print(int(line.strip(), 16))
