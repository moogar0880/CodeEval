"""There is a game where each player picks a number from 1 to 9, writes it on a
paper and gives to a guide. A player wins if his number is the lowest unique.
We may have 10-20 players in our game.
"""
import sys

for line in open(sys.argv[1], 'r'):
    if line.strip() != '':
        nums = dict()
        inputs = line.split(' ')
        for num in inputs:
            if num not in nums:
                nums[num] = 1
            else:
                del nums[num]
        low = None
        for key in nums.keys():
            if low:
                if int(key) < low:
                    low = int(key)
            else:
                low = int(key)
        if not low:
            print 0
        else:
            print low
