from typing import Literal

with open("./inputTest.txt") as file:
    lines = list(map(lambda s: s.removesuffix("\n"), file.readlines()))

startingPosition = None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            startingPosition = (i, j)

if startingPosition is None:
    raise ValueError("Starting position was not found")

distMap = [[-1 for _ in range(len(lines[0]))] for _ in range(len(lines))]
distMap[startingPosition[0]][startingPosition[1]] = 0

toDiscover: list[tuple[int, int]] = [startingPosition]


def get_neighbours(pos: tuple[int, int], pos_map: list[list[int]]):
    h = len(pos_map)
    w = len(pos_map[0])
    x, y = pos

    res: dict[tuple[int, int], int] = {}

    if x > 0:
        res[(x - 1, y)] = pos_map[x - 1][y]
    if y > 0:
        res[(x, y - 1)] = pos_map[x][y - 1]
    if x < w - 1:
        res[(x + 1, y)] = pos_map[x + 1][y]
    if y < h - 1:
        res[(x, y + 1)] = pos_map[x][y + 1]

    return res


# .....
# .S-7.
# .|.|.
# .L-J.
# .....

direction = Literal["left"] | Literal["right"] | Literal["down"] | Literal["up"]


def get_connected_sides(char: str) -> list[direction]:
    dirs_map: dict[str, list[direction]] = {
        "S": ["down", "up", "left", "right"],
        "-": ["left", "right"],
        "|": ["up", "down"],
        "F": ["right", "down"],
        "7": ["down", "left"],
        "L": ["up", "right"],
        "J": ["up", "left"],
    }
    return dirs_map.get(char, [])


def is_connected(position1: tuple[int, int], position2: tuple[int, int]):
    char1_connections = get_connected_sides(lines[position1[0]][position1[1]])
    char2_connections = get_connected_sides(lines[position2[0]][position2[1]])

    print(position1, char1_connections, lines[position1[0]][position1[1]])
    print(position2, char2_connections, lines[position2[0]][position2[1]])
    print()

    if position1[0] != position2[0] and position1[1] != position2[1]:
        raise ValueError(f"{position1} and {position2} are not next to one another")
    if position1[1] < position2[1]:
        if "right" in char1_connections and "left" in char2_connections:
            return True
    if position1[1] > position2[1]:
        if "left" in char1_connections and "right" in char2_connections:
            return True
    if position1[0] < position2[0]:
        if "down" in char1_connections and "up" in char2_connections:
            return True
    if position1[0] > position2[0]:
        if "up" in char1_connections and "down" in char2_connections:
            return True


highest_value = 0

while len(toDiscover) > 0:
    discovering = toDiscover.pop(0)
    neighbours = get_neighbours(discovering, distMap)
    # filter out neighbours that are not connected to the current position
    a = filter(lambda pos: is_connected(pos, discovering), list(neighbours.keys()))
    print(list(a))
    # find all connected neighbours that have a (current value + 1) higher than our current value
    #     assign them a new value and add their position to the list ot toDiscover
    #     if their new value is higher than the highest value then change the highestValue
