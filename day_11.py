import re
import string

def find_passwords(data, alphabet):  
    data_nr = []
    for i in data:
        data_nr.append(alphabet.index(i) + 1)

    passwords = []
    passnr = data_nr.copy()
    while True:
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
        word = create_word(passnr_new, alphabet)
        if check_forbidden(word) and check_double(word) and check_combinations(word, alphabet):
            passwords.append(word)

        if len(passwords) == 2:
            return passwords

def create_word(new_nr, alphabet):
    word = ''
    for j in new_nr:
        word += alphabet[j - 1]
    return word

def check_forbidden(word, forbidden = ['i', 'l', 'o']):
    if all(forbidden not in list(word) for symbol in forbidden):
        return True
    return False

def check_double(word):
    if len(re.findall(r"(\w)(\1)", word)) == 2:
        return True
    return False

def check_combinations(word, alphabet):
    combinations = []
    for i in range(24):
        combinations.append(alphabet[i] + alphabet[i+1] + alphabet[i+2])

    if any(combi in word for combi in combinations):
        return True
    return False


if __name__ == "__main__":
    #  DATA
    with open('./data/data_11.txt') as f:
        data = f.read().strip()

    alphabet = string.ascii_lowercase
    passwords = find_passwords(data, alphabet)
    print(f"Part 1 {passwords[0]}")
    print(f"Part 2 {passwords[1]}")
