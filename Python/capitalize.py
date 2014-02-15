"""Write a program which capitalizes the first letter of each word in a
sentence.

Your program should accept as its first argument a path to a filename.

Print capitalized words.
"""
import sys
import string

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        print(string.replace(' '.join([w.capitalize() for w in line.split(' ')]), '\n', ''))
