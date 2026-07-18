with open("./data/data_02.txt", encoding="utf-8") as f:
    data = f.readlines()

sizes = []
for i in data:
    row = i.strip().split("x")
    sizes.append(list(map(int, row)))

# area =  2*l*w + 2*w*h + 2*h*l + area smallest side, data is stored as lwh
# ribbon = shortest available distance + cubic feet
area = 0
ribbon = 0
for item in sizes:
    smallest_side_info = sorted(item)
    area += (
        2 * item[0] * item[1] 
        + 2 * item[1] * item[2] 
        + 2 * item[2] * item[0] 
        + smallest_side_info[0] * smallest_side_info[1]
    )
    ribbon += (
        2*smallest_side_info[0] 
        + 2*smallest_side_info[1] 
        + item[0] * item[1] * item[2]
    )
print(f"Part 1 area: {area} sq feet")
print(f"Part 2 ribbon: {ribbon} feet")
