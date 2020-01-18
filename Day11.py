# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 00:26:40 2020

@author: laura
"""

#%% IMPORTS
import re
#%% GOAL 1
"""Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

    hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    abbcegjk fails the third requirement, because it only has one double letter (bb).
    The next password after abcdefgh is abcdffaa.
    The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?"""
#%% DATA
data = "vzbxkghb"
#%% CALC 1
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
    elif eight == 26 and seven <26:
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
    elif eight == 26 and seven == 26 and six == 26 and five == 26 and four == 24 and three < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1   
        three += 1
    elif eight == 26 and seven == 26 and six == 26 and five == 26 and four == 24 and three == 26 and two < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three = 1
        two += 1  
    elif eight == 26 and seven == 26 and six == 26 and five == 26 and four == 24 and three == 26 and two == 26 and one < 26:
        eight = 1
        seven = 1
        six = 1
        five = 1
        four = 1
        three = 1
        two = 1
        one += 1    
    else: print("Error")
    
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
    else: first_selection.append("".join(i))
    
sec_selection = []
for i in first_selection:
    if len(re.findall(r"(\w)(\1)", i)) == 2:
        sec_selection.append(i)
        
combinations = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]

three_selection = []
for i in sec_selection:
    if any(combi in i for combi in combinations):
        three_selection.append(i)

print("Santa's new password is", three_selection[0])
#%% GOAL 2
"""Santa's password expired again. What's the next one?"""
#%% CALC 2
print("Santa's second new password is", three_selection[1])
