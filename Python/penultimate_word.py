"""In this challenge you need to find the longest word in a sentence. If the
sentence has more than one word of the same length you should pick the first
one.

Your program should accept as its first argument a path to a filename. Input
example is the following.

Print the longest word from each line
"""
from __future__ import print_function
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        longest = None
        print(line.split(' ')[-2])
