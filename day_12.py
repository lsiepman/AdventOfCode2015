import json
import re


def Red(string):
    if "red" in string.values():
        return {}
    else:
        return string
    
# DATA
with open("./data/data_12.txt") as json_file:
    text = json_file.read()
    json_data = json.loads(text)
    cleaned_text = str(json.loads(text, object_hook=Red))

# Part 1
numbers = re.findall(r"[-0-9]+", text)
total = 0
for i in numbers:
    total = total + int(i)

print(f"Part 1: {total}")


# Part 2  
cleaned_numbers = re.findall(r"[-0-9]+", cleaned_text)
clean_calc = 0
for i in cleaned_numbers:
    clean_calc = clean_calc + int(i)

print(f"Part 2: {clean_calc}")
