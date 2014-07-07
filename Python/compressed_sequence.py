"""Assume that someone dictates you a sequence of numbers and you need to write
it down. For brevity, he dictates it as follows: first says the number of
consecutive identical numbers and then says the number itself.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        results = {}
        longest = None
        for num in line.split(' '):
            if num.strip() not in results:
                results[num.strip()] = 1
            else:
                results[num.strip()] += 1
        output = ''
        for key, val in results.items():
            output += str(val) + ' ' + key + ' '
        print output.strip()
