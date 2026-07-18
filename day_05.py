import re

# DATA
with open("./data/data_05.txt") as f:
    data = f.read().splitlines()

# Part 1
def FindVowelLength(string):
    num_vowels = len(re.findall("[aeiou]", string))
    return num_vowels

def FindDoubleLetter(string):
    do_let = re.findall(r"(\w)(\1)", string)
    return len(do_let) > 0


def ForbiddenCombinations(string):
    matches = re.findall(r"ab|cd|pq|xy", string)
    return len(matches) > 0


vowels = [FindVowelLength(i) for i in data]
double_letter = [FindDoubleLetter(i) for i in data]
forbidden_combos = [ForbiddenCombinations(i) for i in data]

nice_count = 0
for i,j,k in zip(vowels, double_letter, forbidden_combos, strict=True):
    if i >= 3 and j and not k:
        nice_count += 1

print(f"Part 1: {nice_count}")

# Part 2
nice2 = 0
for row in data:
    if (re.search(r"([a-z])([a-z]).*(\1)(\2)", row) 
        and re.search(r"([a-z])([a-z])(\1)", row)):
            nice2 += 1

print(f"Part 2 {nice2}")
