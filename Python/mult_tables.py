CELL = '    '

for i in range(1, 13):
    output = ''
    for j in range(1, 13):
        output += CELL[:-len(str(i * j))] + str(i * j)
    print(output.strip())