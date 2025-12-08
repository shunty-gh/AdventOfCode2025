import math

# Test data
# lines = [
# "162,817,812", "57,618,57", "906,360,560", "592,479,940", "352,342,300",
# "466,668,158", "542,29,236", "431,825,988", "739,650,466", "52,470,668",
# "216,146,977", "819,987,18", "117,168,530", "805,96,715", "346,949,466",
# "970,615,88", "941,993,340", "862,61,35", "984,92,344", "425,690,689",
# ]
# part1_range = 10

part1_range = 1000
with open(f'../input/day08-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Parse all co-ords
coords = list[tuple[int,int,int]]()
for line in lines:
    x,y,z = [int(n) for n in line.split(',')]
    coords.append((x,y,z))

# Create a list of distances between each pairing, sorted by shortest distance
dists = list()
for i,(x0,y0,z0) in enumerate(coords):
    for j,(x1,y1,z1) in enumerate(coords[i+1:]):
        dist = math.sqrt(math.pow(x0-x1,2) + math.pow(y0-y1,2) + math.pow(z0-z1,2))
        dists.append((dist, (x0,y0,z0), (x1,y1,z1)))
dists.sort(key=lambda x: x[0])

# Build up chains of closest pairings
part1, part2 = 0, 0
chains = list[set[tuple[int,int,int]]]()
for i,(_,c1,c2) in enumerate(dists):
    done = False
    must_remove = False

    for ci,chain in enumerate(chains):
        # Part 2 - find last pair to make the complete chain
        if len(chain) == len(coords)-1:
            # Last junction box coming up
            # One or other end of this pair must already be in the chain
            part2 = c1[0] * c2[0]

        if c1 in chain or c2 in chain:
            if not done:
                # Chain is a set() so we can try to add both elements without increasing the size
                chain.add(c1)
                chain.add(c2)
                target_chain = chain # Save this in case we need to merge another chain
                done = True
            else:
                # We've found a second chain that contains one of the elements.
                # We need to merge this chain into the previous chain, then delete
                # this one. Don't delete it while we're iterating through them
                # though.
                target_chain.update(chain)
                to_remove = ci
                must_remove = True

    if must_remove:
        del chains[to_remove]

    if not done:
        # Neither end is in an existing chain so start a new one
        chains.append(set([c1,c2]))

    # Part 1
    if i == part1_range-1:
        # Sort them by chain length
        chains.sort(key=lambda x: len(x), reverse=True)
        part1 = math.prod([len(chain) for chain in chains[:3]])

print("Part 1:", part1)
print("Part 2:", part2)
