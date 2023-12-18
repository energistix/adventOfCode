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

newLines: list[str] = []

for i, line in enumerate(lines):
    l = ""
    for j, char in enumerate(line):
        if j in emptyColumns:
            l += char
        l += char
    if i in emptyLines:
        newLines.append(l)
    newLines.append(l)

lines = newLines
del newLines

galaxies: list[tuple[int, int]] = []

for i, line in enumerate(lines):
    galaxies.extend((i, j) for j, char in enumerate(line) if char == "#")
total = 0

for combination in combinations(galaxies, 2):
    g1, g2 = combination
    x1, y1 = g1
    x2, y2 = g2
    total += abs(x2 - x1) + abs(y2 - y1)

print(total)
