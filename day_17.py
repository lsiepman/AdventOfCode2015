from collections import Counter
from itertools import combinations

# DATA
data = []
with open("./data/data_17.txt") as file:
    for line in file:
        data.append(int(line))

# Part 1
result = [
    seq
    for i in range(len(data), 0, -1)
    for seq in combinations(data, i)
    if sum(seq) == 150
]
print(f"Part 1: {len(result)}")

# Part 2
lengths = []
for i in result:
    lengths.append(len(i))

print(f"Part 2: {Counter(lengths)[4]}")
