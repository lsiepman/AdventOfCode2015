import math

# Data
with open("./data/data_20.txt") as file:
    data = int(file.read())

# Part 1
def CalcPresents(x, mult=10):
    total = 0
    limit = int(math.isqrt(x))
    
    for i in range(1, limit + 1):
        if x % i == 0:
            total += i
            # Add the paired factor if it's not a perfect square
            if i != x // i:
                total += x // i

    return total * mult


j = 0
result = 0

while result < data:
    j += 1
    result = CalcPresents(j, 10)

print(f"Part 1: {j}")

# Part 2
def CalcPresentsPart2(x, mult=11):
    total = 0
    limit = int(math.isqrt(x))
    
    for i in range(1, limit + 1):
        if x % i == 0:
            paired_factor = x // i
            
            # Check if the factor 'i' is within its first 50 stops
            if paired_factor <= 50:
                total += i
                
            # Check if the paired factor is within its first 50 stops
            if i <= 50 and i != paired_factor:
                total += paired_factor

    return total * mult

j = 0
result = 0

while result < data:
    j += 1
    result = CalcPresentsPart2(j, 11)

print(f"Part 2: {j}")
