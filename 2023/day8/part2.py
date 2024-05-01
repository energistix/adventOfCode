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

curentPositions = list(filter(lambda k: k.endswith("A"), positions.keys()))

ended = False
i = 0

nextImportantPoint = 10

while not ended:
    if i == nextImportantPoint:
        print(i)
        print(curentPositions)
        nextImportantPoint *= 10
    ended = True
    nextPositions: list[str] = []
    for curentPosition in curentPositions:
        nextPositions.append(positions[curentPosition][path[i % len(path)] == "R"])
        if not nextPositions[-1].endswith("Z"):
            ended = False
    curentPositions = nextPositions
    i += 1

print(i)
