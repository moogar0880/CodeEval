"""Given a string write a program to convert it into lowercase.

The first argument will be a path to a filename containing sentences, one per
line. You can assume all characters are from the english language.

Print to stdout, the lowercase version of the sentence, each on a new line
"""
import sys
import string

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        print string.replace(line.lower(), '\n', '')
