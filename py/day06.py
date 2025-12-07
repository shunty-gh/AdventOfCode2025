import math
import re

# test data
lines = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "
]

with open(f'../input/day06-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

allvals = list()
opline = lines[-1]
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

part2 = 0
# first find the index of each operator - this is where each number section will start
# then read in the numbers in each block - including leading space
# This is a bit arse about face but who cares
ops = list[tuple[int,str]]()
for i,ch in enumerate(opline):
    if ch in { '+', '*'}:
        ops.append((i, ch))

numrows = len(lines)-1
prev = 0
for i,(start,op) in enumerate(ops):
    nums = list[int]()
    idx = ops[i+1][0]-2 if i < len(ops)-1 else len(lines[0])-1
    while idx >= start:
        nstr = ''.join ([nn for nn in [s[idx] for s in lines[:-1]]])
        nums.append(int(nstr.strip()))
        idx -= 1

    if op == '+':
        part2 += sum(nums)
    else:
        rval = 1
        part2 += math.prod(nums)

print("Part 2:", part2)
