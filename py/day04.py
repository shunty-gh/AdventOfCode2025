with open(f'../input/day04-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

delta = { (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1) }
numlines = len(lines)
part1 = 0
for y in range(len(lines)):
    line = lines[y]
    ll = len(line)
    for x,ch in enumerate(line):
        if ch != '@':
            continue
        neigh = 0

        for dx,dy in delta:
            px,py = x+dx, y+dy
            if px >= 0 and py >= 0 and px < ll and py < numlines and lines[py][px] == '@':
                neigh += 1
        if neigh < 4:
            part1 += 1

print("Part 1:", part1) # 10254, 2614 too high
