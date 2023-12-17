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


def is_connected(position1: tuple[int, int], position2: tuple[int, int]):
    # looks at the pipes at those positions to see of they connect
    pass


highest_value = 0

while len(toDiscover) > 0:
    discovering = toDiscover.pop(0)
    neighbours = get_neighbours(discovering, distMap)
    # filter out neighbours that are not connected to the current position
    # find all connected neighbours that have a (current value + 1) higher than our current value
    #     assign them a new value and add their position to the list ot toDiscover
    #     if their new value is higher than the highest value then change the highestValue
