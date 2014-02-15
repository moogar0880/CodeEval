"""Write a program to reverse the words of an input sentence.

The first argument will be a path to a filename containing multiple sentences,
one per line. Possibly empty lines too.

Print to stdout, each line with its words reversed, one per line. Empty lines
in the input should be ignored. Ensure that there are no trailing empty spaces
on each line you print.
"""
import sys
import string

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        print string.replace(' '.join(line.split(' ')[::-1]), '\n', '').strip()
