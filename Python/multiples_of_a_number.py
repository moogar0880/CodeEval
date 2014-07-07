import sys

for line in open(sys.argv[1], 'r'):
    if line.strip():
        x, n = [int(i) for i in line.strip().split(',')]
        val = n
        while val < x:
            val += n
        print(val)
