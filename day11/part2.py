import os
from itertools import combinations

os.system("cls" if os.name == "nt" else "clear")

with open("./input.txt", "r") as file:
    lines = list(map(lambda s: s.removesuffix("\n"), file.readlines()))

emptyLines: list[int] = [
    i for i, line in enumerate(lines) if all(map(lambda s: s == ".", line))
]

emptyColumns = [
    i
    for i in range(len(lines[0]))
    if all(map(lambda s: s == ".", [lines[j][i] for j in range(len(lines))]))
]


galaxies: list[tuple[int, int]] = []

for i, line in enumerate(lines):
    galaxies.extend((i, j) for j, char in enumerate(line) if char == "#")

total = 0

for combination in combinations(galaxies, 2):
    g1, g2 = combination
    x1, y1 = g1
    x2, y2 = g2

    if x2 < x1:
        x2, x1 = x1, x2
    if y2 < y1:
        y2, y1 = y1, y2

    nbr_empty_lines_between = len([n for n in emptyLines if x1 < n < x2])
    nbr_empty_cols_between = len([n for n in emptyColumns if y1 < n < y2])

    distx = x2 - x1
    disty = y2 - y1

    total += distx + disty + (nbr_empty_cols_between + nbr_empty_lines_between) * 999999

print(total)
