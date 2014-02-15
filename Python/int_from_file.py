"""Print out the sum of integers read from a file.

The first argument to the program will be a path to a filename containing a
positive integer, one per line.

Print out the sum of all the integers read from the file.
"""
import sys
from __future__ import print_function

total = 0
for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        total += int(line)
print(total)
