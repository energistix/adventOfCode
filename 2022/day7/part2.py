import json
import re

with open("./input.txt") as file:
    lines = file.readlines()

path = []

folderTree = {}


def set_value(path: list[str], obj: dict, value: int):
    p = path.pop(0)
    if p not in obj.keys():
        obj[p] = {} if path else value
    if path:
        set_value(path, obj[p], value)


folder_weights = []


def calculate_folder_weight(folder: dict):
    res = 0
    for k in folder:
        if isinstance(folder[k], int):
            res += folder[k]
        elif isinstance(folder[k], dict):
            res += calculate_folder_weight(folder[k])
    folder_weights.append(res)
    return res


for line in lines:
    if m := re.match(r"\$ cd (.+)", line):
        p = m.groups()[0]
        if p == "..":
            path.pop()
        else:
            path.append(p)
    elif m := re.match(r"(\d+) (.+)", line):
        weight, name = m.groups()
        set_value(path + [name], folderTree, int(weight))

print(json.dumps(folderTree, indent=2))
calculate_folder_weight(folderTree)

total_weight = max(folder_weights)
available_space = 70_000_000 - total_weight
needed_space = 30_000_000 - available_space

print(min(filter(lambda w: w > needed_space, folder_weights)))
