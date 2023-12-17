with open("./input.txt", "r") as file:
    lines = file.readlines()

lists: list[list[int]] = [
    list(map(int, line.removesuffix("\n").split(" "))) for line in lines
]
total = 0

lines.reverse()

for curr_list in lists:
    first_values = [curr_list[0]]
    while any(map(lambda n: n != 0, curr_list)):
        new_list: list[int] = [
            curr_list[i] - curr_list[i - 1] for i in range(1, len(curr_list))
        ]
        curr_list = new_list
        first_values.append(curr_list[0])
    current_value = 0
    for i in range(len(first_values) - 1, -1, -1):
        current_value = first_values[i] - current_value
    total += current_value
print(total)
