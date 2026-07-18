import re

# Read data
with open("./data/data_01.txt", encoding='utf-8') as f:
    data = f.read()


# Part 1
up = len(re.findall(r"\(", data))
down = len(re.findall(r"\)", data))
floor = up - down
print(f"Part 1 floor = {floor}")

# Part 2
now = 0
i = 0
while now != -1:
    if re.search(r"\(", data[i]):
        now += 1
    else:
        now -= 1

    i += 1

print(f"Part 2 position = {i}")
