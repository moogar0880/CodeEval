"""You are given a string 'S' and a character 't'. Print out the position of
the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none.
The position to be printed out is zero based.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        out = ''
        string, char = tuple(line.split(','))
        print len(string) - string[::-1].strip().find(char.strip()) - 1
