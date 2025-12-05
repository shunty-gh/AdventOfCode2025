with open(f'../input/day05-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

part1 = 0
fresh = set()
for line in lines:
    if '-' in line:
        ll,rr = line.split('-')
        fresh.add((int(ll), int(rr)))
    else:
        if len(line) < 1:
            continue
        ingredient = int(line)
        for lo,hi in fresh:
            if ingredient >= lo and ingredient <= hi:
                part1 += 1
                break

print("Part 1:", part1)
