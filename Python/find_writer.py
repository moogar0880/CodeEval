"""You have a set of rows with names of famous writers encoded inside. Each row
is divided into 2 parts by pipe char (|). The first part has a writer's name.
The second part is a "key" to generate a name.

Your goal is to go through each number in the key (numbers are separated by
space) left-to-right. Each number represents a position in the 1st part of a
row. This way you collect a writer's name which you have to output.

Your program should accept as its first argument a path to a filename.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        out = ''
        letters, indicies = tuple(line.split('|'))
        indicies = [index.strip() for index in indicies.split(' ') if index != '']
        for index in indicies:
            out += letters[int(index) - 1]
        print(out)
