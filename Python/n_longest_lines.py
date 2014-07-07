import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
n = int(lines[0])
del lines[0]
lines = sorted(lines, key=len)[-n:][::-1]
for word in lines:
    print(word.strip())
