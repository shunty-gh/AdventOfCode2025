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

# Part 2 - Load all the ranges then split them up into a set of distinct, non-overlapping ranges
allranges = set()
for line in lines:
    if not '-' in line:
        break
    ll,rr = line.split('-')
    allranges.add((int(ll), int(rr)))

# allranges now acts as a queue of sub-ranges that need to be processed
fresh = set()
while len(allranges) > 0:
    lo, hi = allranges.pop()
    # Check for overlaps
    ok = True
    for flo,fhi in fresh:
        # Exact match or completely contained -> ignore it completely
        if lo >= flo and hi <= fhi:
            ok = False
            break
        # All above or all below -> try against the next saved range
        if lo > fhi or hi < flo:
            continue

        # Must be an intersection
        # Split into new ranges and add them to the queue for further processing
        # lower range
        if lo < flo:
            allranges.add((lo, flo-1))
        # upper range
        if hi > fhi:
            allranges.add((fhi+1, hi))
        ok = False
        break

    # no part of the current range appears in any existing saved 'fresh' range, therefore add it
    if ok:
        fresh.add((lo, hi))

part2 = sum([hi-lo+1 for lo,hi in fresh])
print("Part 2:", part2)
