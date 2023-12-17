with open("./input.txt", "r") as file:
    lines = file.readlines()

lists: list[list[int]] = [
    list(map(int, line.removesuffix("\n").split(" "))) for line in lines
]
total = 0

for curr_list in lists:
    last_values = [curr_list[-1]]
    while any(map(lambda n: n != 0, curr_list)):
        new_list: list[int] = [
            curr_list[i] - curr_list[i - 1] for i in range(1, len(curr_list))
        ]
        curr_list = new_list
        last_values.append(curr_list[-1])
    total += sum(last_values)

print(total)
