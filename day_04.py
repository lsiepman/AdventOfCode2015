from hashlib import md5

with open("./data/data_04.txt", encoding="utf-8") as f:
    data = f.read().strip()

# Part 1
for i in range(1, 1000000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()

    if hashhex.startswith("00000"):
        print(f"Part 1: {i}")
        break

# Part 2
for j in range(1, 100000000):
    fullstr = data + str(j)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()

    if hashhex.startswith("000000"):
        print(f"Part 2: {j}")
        break
