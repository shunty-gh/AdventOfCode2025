import os

#test_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#lines = test_data.strip().split(',')

with open(f'../input/day02-input', 'r') as file:
    input = file.read().strip()
    lines = input.split(',')

part1 = 0
for line in lines:
    lo, hi = line.split('-')
    nlo, nhi = int(lo), int(hi)
    for n in range(nlo, nhi + 1):
        nstr = str(n)
        if len(nstr) % 2 == 0:
            mid = len(nstr) // 2
            if nstr[:mid] == nstr[mid:]:
                part1 += n

print("Part 1:", part1)

part2 = 0
for line in lines:
    lo, hi = line.split('-')
    nlo, nhi = int(lo), int(hi)
    for n in range(nlo, nhi + 1):
        nstr = str(n)
        match = False
        for i in range(len(nstr)//2):
            key = nstr[:i+1]
            cmp = key
            while len(cmp) < len(nstr):
                cmp += key
                if cmp == nstr:
                    part2 += n
                    match = True
                    break
            if match:
                break

print("Part 2:", part2)
