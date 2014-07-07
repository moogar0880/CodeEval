"""Write a program which capitalizes the first letter of each word in a
sentence.

Your program should accept as its first argument a path to a filename.

Print capitalized words.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip():
        output = ''
        for word in line.split():
            output += word[0].capitalize() + word[1:] + ' '
        print(output[:-1])
