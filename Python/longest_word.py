"""In this challenge you need to find the longest word in a sentence. If the
sentence has more than one word of the same length you should pick the first
one.

Your program should accept as its first argument a path to a filename. Input
example is the following.

Print the longest word from each line
"""
import sys
import string

longest_words = []
for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        longest = None
        for word in line.split(' '):
            if longest:
                if len(word.strip()) > len(longest):
                    longest = word.strip()
            else:
                longest = word.strip()
        longest_words.append(longest)
print '\n'.join(longest_words)
