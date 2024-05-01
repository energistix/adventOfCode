positions: dict[str, tuple[str, str]] = {}


with open("./input.txt", "r") as file:
    lines = list(file.readlines())

path = lines.pop(0).replace("\n", "")
lines.pop(0)

for line in lines:
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    line = line.replace("(", "")
    line = line.replace(")", "")

    position, destinations = line.split("=")
    left, right = destinations.split(",")

    positions[position] = (left, right)

curentPosition = "AAA"

i = 0
while curentPosition != "ZZZ":
    if path[i % len(path)] == "L":
        curentPosition = positions[curentPosition][0]
    else:
        curentPosition = positions[curentPosition][1]
    i += 1

print(i)
