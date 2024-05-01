# 15415806 is too low

from typing import TypedDict


class NumberType(TypedDict):
    id: int
    value: int
    valueStr: str


lines = []
numbers: dict[str, NumberType] = {}
nextId = 0

with open("./input.txt") as file:
    lines = list(file.readlines())

currentNumber: NumberType = {"id": nextId, "value": 0, "valueStr": ""}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char.isdigit():
            currentNumber["valueStr"] += char
            numbers[f"{i}:{j}"] = currentNumber
        elif len(currentNumber["valueStr"]) > 0:
            currentNumber["value"] = int(currentNumber["valueStr"])
            nextId += 1
            currentNumber = {"id": nextId, "value": 0, "valueStr": ""}

total = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "*":
            localNumbers: dict[int, NumberType] = {}
            for x in range(-1, 2):
                x += j
                for y in range(-1, 2):
                    y += i
                    if x < 0 or x >= len(line) or y < 0 or y >= len(lines):
                        continue
                    if f"{y}:{x}" in numbers.keys():
                        nbr = numbers[f"{y}:{x}"]
                        localNumbers[nbr["id"]] = nbr
            if len(localNumbers) == 2:
                values = list(map(lambda n: n["value"], localNumbers.values()))
                total += values[0] * values[1]

# numbersByIds = {
#     id: number for (id, number) in map(lambda nbr: (nbr["id"], nbr), numbers.values())
# }
#
# for id, nbr in numbersByIds.items():
#     print(id, nbr)
#     if id > 1000:
#         break

# for id, nbr in numbers.items():
#     print(id, nbr)
#     if nbr["id"] > 100:
#         break

print(total)
