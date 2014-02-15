"""Given a positive integer, find the sum of its constituent digits.

The first argument will be a path to a filename containing positive integers,
one per line

Print to stdout, the sum of the numbers that make up the integer, one per line
"""
import sys

def to_base_x(num, base):
    output = []
    while num:
        num, rem = divmod(num, base)
        output.append(rem)
    return output

def sum_digits(num, base=10):
    if base < 2:
        print "Error: Base must be at least 2"
        return
    return sum(to_base_x(num, base))

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        print sum_digits(int(line))