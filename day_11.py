import re
import string

#  DATA
with open('./data/data_11.txt') as f:
    data = f.read().strip()
# Part 1
alphabet = string.ascii_lowercase
data_nr = []
for i in data:
    data_nr.append(alphabet.index(i) + 1)

new_nr = []
passnr = data_nr.copy()
for i in range(3000000):
    eight = passnr[7]
    seven = passnr[6]
    six = passnr[5]
    five = passnr[4]
    four = passnr[3]
    three = passnr[2]
    two = passnr[1]
    one = passnr[0]

    if eight < 26:
        eight += 1
    elif seven < 26:
        eight = 1
        seven += 1
    elif six < 26:
        eight = 1
        seven = 1
        six += 1
    elif five < 26:
        eight = 1
        seven = 1
        six = 1
        five += 1
    elif four < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four += 1
    elif three < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three += 1
    elif two < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three = 1
        two += 1
    elif one < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three = 1
        two = 1
        one += 1
    else:
        print("Error")

    passnr[7] = eight
    passnr[6] = seven
    passnr[5] = six
    passnr[4] = five
    passnr[3] = four
    passnr[2] = three
    passnr[1] = two
    passnr[0] = one

    passnr_new = passnr.copy()

    new_nr.append(passnr_new)

new_words = []
for i in new_nr:
    word = []
    for j in i:
        word.append(alphabet[j - 1])
    new_words.append(word)

forbidden = ['i', 'l', 'o']
first_selection = []
for i in new_words:
    if all(forbidden not in i for symbol in forbidden):
        first_selection.append("".join(i))

sec_selection = []
for i in first_selection:
    if len(re.findall(r"(\w)(\1)", i)) == 2:
        sec_selection.append(i)

combinations = []
for i in range(24):
    combinations.append(alphabet[i] + alphabet[i+1] + alphabet[i+2])

three_selection = []
for i in sec_selection:
    if any(combi in i for combi in combinations):
        three_selection.append(i)

print(f"Part 1 {three_selection[0]}")
print(f"Part 2 {three_selection[1]}")
