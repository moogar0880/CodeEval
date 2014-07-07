"""There is a game where each player picks a number from 1 to 9, writes it on a
paper and gives to a guide. A player wins if his number is the lowest unique.
We may have 10-20 players in our game.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        a, b, n = [int(var) for var in line.split()]
        out = ''
        for i in range(1, n + 1):
            if i % a == 0 and i % b == 0:
                out += 'FB '
            elif i % a == 0:
                out += 'F '
            elif i % b == 0:
                out += 'B '
            else:
                out += '%d ' % i
        print(out.strip())
