with open(f'../input/day04-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

delta = { (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1) }
ylen, xlen = len(lines), len(lines[0])
removed, toremove, found = set(), set(), 1
part1 = 0
while found != 0:
    found = 0
    for y,line in enumerate(lines):
        for x,ch in enumerate(line):
            if ch != '@' or (x,y) in removed:
                continue

            neigh = 0
            for px,py in [(x+dx,y+dy) for dx,dy in delta]:
                if (px,py) not in removed and px >= 0 and py >= 0 and px < xlen and py < ylen and lines[py][px] == '@':
                    neigh += 1

            if neigh < 4:
                toremove.add((x,y))

    found = len(toremove)
    if part1 == 0:
        part1 = found

    removed.update(toremove)
    toremove.clear()

print("Part 1:", part1)
print("Part 2:", len(removed))
