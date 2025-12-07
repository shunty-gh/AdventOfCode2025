
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

# Recursion and memoisation. The definition of hell on earth.
# But it sure is quick.
cache = dict[tuple[int,int], int]()
def get_timelines_from(manifold: list[str], x: int, y: int) -> int:
    # Have we seen this already
    if (x,y) in cache:
        return cache[(x,y)]

    # Is next row the exit row?
    if y+1 == len(manifold)-1:
        return 1

    # Cursed recursion. Find count from this col, or the left and right
    # cols if there is a splitter directly below us
    if manifold[y+1][x] == '^':
        result = get_timelines_from(manifold, x-1, y+1) + get_timelines_from(manifold, x+1, y+1)
    else:
        result = get_timelines_from(manifold, x, y+1)
    # Cache and return
    cache[(x,y)] = result
    return result

print("Part 2:", get_timelines_from(lines, start, 0))
