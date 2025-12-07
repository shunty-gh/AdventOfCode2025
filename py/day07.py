import re

with open(f'../input/day07-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

part1 = 0
start = lines[0].index("S")
current = set()
current.add(start)
next = set()
for y,line in enumerate(lines[1:]):
    next.clear()
    next.update(current)
    if (line.find('^') < 0):
        continue
    splitters = [i for i,v in enumerate(line) if v == "^"]
    for splitter in splitters:
        if (splitter) in current:
            # Split it
            next.remove(splitter)
            next.add(splitter-1)
            next.add(splitter+1)
            part1 += 1
    current.clear()
    current.update(next)

print("Part 1:", part1)
