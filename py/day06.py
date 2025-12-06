import re

with open(f'../input/day06-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

allvals = list()
for line in lines:
    if line[0] in { '+', '*'}:
        ops = re.findall('(\*|\+)', line)
        allvals.append(ops)
        break
    vals = list(map(int, line.split()))
    allvals.append(vals)

part1 = 0
avlen = len(allvals)
rlen = len(allvals[0])
for x in range(rlen):
    op = allvals[avlen-1][x]
    if op == '+':
        rval = 0
        for y in range(avlen-1):
            rval += allvals[y][x]
        part1 += rval
    elif op == '*':
        rval = 1
        for y in range(avlen-1):
            rval *= allvals[y][x]
        part1 += rval
    else:
        print("Unknown symbol", op)
        break

print("Part 1:", part1)
