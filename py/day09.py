import math

with open(f'../input/day09-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Parse all co-ords
coords = list[tuple[int,int,int]]()
for line in lines:
    x,y = [int(n) for n in line.split(',')]
    coords.append((x,y))

#print(coords)
# Create a list of areas between each pairing, sorted by biggest
areas = list()
maxarea = 0
for i,(x0,y0) in enumerate(coords):
    for j,(x1,y1) in enumerate(coords[i+1:]):
        sz = (abs(x0-x1)+1) * (abs(y0-y1)+1)
        if sz > maxarea:
            maxarea = sz
        areas.append((sz, (x0,y0), (x1,y1)))
areas.sort(key=lambda x: x[0], reverse=True)

print("Part 1:", maxarea)
print("Part 1:", areas[0])
