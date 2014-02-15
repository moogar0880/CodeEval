"""You have 2 lists of positive integers. Write a program which multiplies
corresponding elements in these lists.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        left, right = tuple(line.split('|'))
        left = left.strip().split(' ')
        right = right.strip().split(' ')
        results = []
        for index, num in enumerate(left):
            results.append(int(num) * int(right[index]))
        out = ''
        for result in results:
            out += str(result) + ' '
        print(out.strip())
