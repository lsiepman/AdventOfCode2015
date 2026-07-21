from itertools import groupby

# DATA
with open('./data/data_10.txt') as f:
    data = f.read().strip()

# Part 1
seq = data
for _ in range(40):
    string = []
    for k, g in groupby(seq):
        output = str(len(list(g))) + k
        string.append(output)
    seq = "".join(string)

print(f"Part 1: {len(seq)}")


# Part 2
seq = data
for _ in range(50):
    string = []
    for k, g in groupby(seq):
        output = str(len(list(g))) + k
        string.append(output)
    seq = "".join(string)

print(f"Part 2: {len(seq)}")
