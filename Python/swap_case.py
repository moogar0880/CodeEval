"""Write a program which swaps letters' case in a sentence. All non-letter
characters should remain the same.

Your program should accept as its first argument a path to a filename.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        out = ''
        for char in line.strip():
            if char != '':
                if char.isupper():
                    out += char.lower()
                else:
                    out += char.upper()
        print(out)
