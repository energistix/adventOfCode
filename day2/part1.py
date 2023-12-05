lines: list[str] = []
with open("./day2/input.txt", "r") as f:
    lines = f.readlines()


colorsMaxs = {"red": 12, "green": 13, "blue": 14}
colorsList = list(colorsMaxs.keys())


def parseInt(string: str):
    res = ""
    for char in string:
        if char.isdigit():
            res += char
        else:
            break
    return res


def parseGame(string: str) -> tuple[dict[str, int], str]:
    balloons: dict[str, int] = {}
    while not string.startswith(";") and len(string) > 0:
        color, ammount, string = parseBalloon(string)
        balloons[color] = ammount

        if string.startswith(","):
            string = string.replace(",", "", 1)
    string = string.replace(";", "", 1)
    return balloons, string


def parseColor(string: str):
    validColors = list(filter(lambda s: string.startswith(s), colorsList))
    if len(validColors) == 1:
        return validColors[0]
    raise ValueError(f"There should be a color at the start of {string}")


def parseBalloon(string: str) -> tuple[str, int, str]:
    ammount = parseInt(string)
    string = string.replace(ammount, "", 1)
    color = parseColor(string)
    string = string.replace(color, "", 1)

    return color, int(ammount), string


total: int = 0

for line in lines:
    line = line.replace("Game", "", 1)
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    gameid = parseInt(line)
    line = line.replace(f"{gameid}:", "", 1)

    possible = True

    while len(line) > 0 and possible:
        game, line = parseGame(line)
        for color, max in colorsMaxs.items():
            if color in game and game[color] > max:
                possible = False
                break

    if possible:
        total += int(gameid)

    print(f"{gameid} : {line}")

print(total)
