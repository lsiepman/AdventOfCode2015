# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 00:26:40 2020

@author: laura
"""

# %% IMPORTS
import re

# %% DATA
data = "vzbxkghb"
# %% CALC 1
alphabet = "0abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)

data_list = list(data)

data_nr = []
for i in data_list:
    data_nr.append(alphabet.index(i))

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
    elif eight == 26 and seven < 26:
        eight = 1
        seven += 1
    elif eight == 26 and seven == 26 and six < 26:
        eight = 1
        seven = 1
        six += 1
    elif eight == 26 and seven == 26 and six == 26 and five < 26:
        eight = 1
        seven = 1
        six = 1
        five += 1
    elif eight == 26 and seven == 26 and six == 26 and five == 26 and four < 24:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four += 1
    elif (
        eight == 26
        and seven == 26
        and six == 26
        and five == 26
        and four == 24
        and three < 26
    ):
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three += 1
    elif (
        eight == 26
        and seven == 26
        and six == 26
        and five == 26
        and four == 24
        and three == 26
        and two < 26
    ):
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three = 1
        two += 1
    elif (
        eight == 26
        and seven == 26
        and six == 26
        and five == 26
        and four == 24
        and three == 26
        and two == 26
        and one < 26
    ):
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
        word.append(alphabet[j])
    new_words.append(word)

first_selection = []
for i in new_words:
    if "i" in i or "l" in i or "o" in i:
        print("removing")
    else:
        first_selection.append("".join(i))

sec_selection = []
for i in first_selection:
    if len(re.findall(r"(\w)(\1)", i)) == 2:
        sec_selection.append(i)

combinations = [
    "abc",
    "bcd",
    "cde",
    "def",
    "efg",
    "fgh",
    "ghi",
    "hij",
    "ijk",
    "jkl",
    "klm",
    "lmn",
    "mno",
    "nop",
    "opq",
    "pqr",
    "qrs",
    "rst",
    "stu",
    "tuv",
    "uvw",
    "vwx",
    "wxy",
    "xyz",
]

three_selection = []
for i in sec_selection:
    if any(combi in i for combi in combinations):
        three_selection.append(i)

print("Santa's new password is", three_selection[0])
# %% GOAL 2
"""Santa's password expired again. What's the next one?"""
# %% CALC 2
print("Santa's second new password is", three_selection[1])
