import re

#  DATA
with open("./data/data_25.txt") as file:
    data = file.read()

numbers = re.findall(r"(\d+)", data)
row_data = int(numbers[0])
col_data = int(numbers[1])


def CalcNextCode(code):
    return (code * 252533) % 33554393


def CalcSeq(input_row, input_col, code=20151125):
    row = 1
    col = 1

    while True:
        if row == 1:
            row = col + 1
            col = 1
        else:
            row = row - 1
            col = col + 1

        code = CalcNextCode(code)
        if row == input_row and col == input_col:
            print(f"Part 1: {code}")
            break


CalcSeq(row_data, col_data)
