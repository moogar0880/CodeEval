"""Write a program which checks input numbers and determines whether a number
is even or not.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        if int(line.strip()) % 2 == 0:
            print 1
        else:
            print 0
