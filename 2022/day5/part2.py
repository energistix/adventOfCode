import re

with open("./input.txt") as file:
    lines = file.readlines()

number_of_stacks = len(lines[0]) // 4
stacks = [[] for _ in range(number_of_stacks)]


line_index = 0
while re.match(r"[1-9]", lines[line_index][1]) is None:
    line = lines[line_index]
    line_index += 1

    for i in range(number_of_stacks):
        char = line[i * 4 + 1]
        if re.match(r"[a-zA-Z]", char):
            stacks[i].insert(0, char)

line_index += 2

lines = lines[line_index:]
data: list[list[int]] = []
for line in lines:
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m is not None:
        data.append(list(map(int, m.groups())))


for d in data:
    values = stacks[d[1] - 1][-d[0] :]
    for _ in range(d[0]):
        stacks[d[1] - 1].pop()
    stacks[d[2] - 1].extend(values)

print("".join(map(lambda d: d[-1], stacks)))
