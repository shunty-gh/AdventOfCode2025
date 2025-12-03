
#test_data = "987654321111111,811111111111119,234234234234278,818181911112111" # P1: 357; P2: 3121910778619
#lines = [line.strip() for line in test_data.split(',')]

def find_largest(line: str, length: int) -> int:
    v, l1, linelen = 0, 0, len(line)

    start_idx, joltage = 0, 0
    for i in range(length):
        curr = 0
        # This result index needs at least length-(i+1) characters remaining in the
        # string in order to be able to fill all the remaining result indexes.
        # And we're starting from where the last search left off.
        lim = linelen-(length-(i+1))
        for j in range(start_idx, lim):
            x = int(line[j])
            if (x > curr):
                curr = x
                start_idx = j
        joltage = joltage * 10 + curr
        start_idx += 1
    return joltage

with open(f'../input/day03-input', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

print("Part 1:", sum([find_largest(ln, 2) for ln in lines]))
print("Part 2:", sum([find_largest(ln, 12) for ln in lines]))
