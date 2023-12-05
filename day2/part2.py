from part1 import parseGame, parseInt

lines: list[str] = []

with open("./input.txt") as f:
    lines = list(f.readlines())

total = 0

for line in lines:
    line = line.replace("Game", "", 1)
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    gameid = parseInt(line)
    line = line.replace(f"{gameid}:", "", 1)

    possible = True

    values = {"red": 0, "green": 0, "blue": 0}

    while len(line) > 0 and possible:
        game, line = parseGame(line)
        for color, ammount in game.items():
            if values[color] < ammount:
                values[color] = ammount

    gamePower = values["blue"] * values["green"] * values["red"]

    total += int(gamePower)

    print(f"{gameid} : {line}")

print(total)
