# IMPORTS
import pandas as pd
import re

# DATA
with open("./data/data_08.txt") as file:
    data = file.read().splitlines()

data = pd.DataFrame(data)
data[0] = data[0].str.strip()

# string literals
data["len_literal"] = data[0].apply(len)

def CleanString(string):
    step1 = re.sub(r"\\x[0-9A-Fa-f]{2}", "n", string)
    step2 = re.sub(r"\\{2}", "a", step1)
    step3 = re.sub(r"\\\"", "b", step2)
    step4 = re.sub(r"\"", "", step3)

    return step4

data["clean_string"] = data[0].apply(CleanString)
data["len_string"] = data["clean_string"].apply(len)

len_string = sum(data["len_string"])
len_lit = sum(data["len_literal"])
answer = len_lit - len_string
print("Part 1: {}".format(answer))

# Part 2
def EncodeString(string):
    encoded = string
    encoded = encoded.replace("\\", "\\\\").replace('"', '\\"')
    encoded = '"' + encoded + '"'

    return len(encoded)


data["len_encoded"] = data[0].apply(EncodeString)
print("Part 2 {}".format(sum(data["len_encoded"]) - len_lit))
