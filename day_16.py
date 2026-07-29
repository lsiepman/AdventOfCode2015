import re


# Functions
def check_ticker_part_1(aunt, ticker):
    return all(ticker[cat] == cnt for cat, cnt in aunt.items())

def check_ticker_part_2(aunt, ticker):
    for cat, cnt in aunt.items():
        if cat in ("cats", "trees"):
            if ticker[cat] >= cnt:
                return False
        elif cat in ("pomerians", "goldfish"):
             if ticker[cat] <= cnt:
                return False
        elif ticker[cat] != cnt:
                return False
    return True

# DATA
data = {}
with open("./data/data_16.txt") as file:
    for line in file:
        categories = re.split(r"\W", line)
        sue = int(categories[1])          
        temp = {categories[3]: int(categories[5]), 
                categories[7]: int(categories[9]),
                categories[11]: int(categories[13])}
        data[sue] = temp

# ticker tape
ticker = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1
          }

# Part 1
for k,v in data.items():
    if check_ticker_part_1(v, ticker):
         print(f"Part 1 {k}")
         break
    
# Part 2
for k,v in data.items():
    if check_ticker_part_2(v, ticker):
         print(f"Part 2 {k}")
         break
