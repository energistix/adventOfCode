with open("./input.txt") as file:
    data = file.readlines()

data = list(map(lambda x: list(map(int, [x[i] for i in range(len(data[-1]))])), data))


starting_positions: list[tuple[int, int]] = [
    (0, 0),
    (len(data) - 1, 0),
    (0, 0),
    (0, len(data[-1]) - 1),
]

lead_directions: list[tuple[int, int]] = [
    (0, 1),
    (0, 1),
    (1, 0),
    (1, 0),
]

exploration_directions: list[tuple[int, int]] = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

trees: set[tuple[int, int]] = set()

for i, starting_position in enumerate(starting_positions):
    lead_direction = lead_directions[i]
    exploration_direction = exploration_directions[i]

    starting_y, starting_x = starting_position
    j = 0
    while (
        len(data) > (lead_y := starting_y + (lead_direction[0] * j)) >= 0
        and len(data[-1]) > (lead_x := starting_x + (lead_direction[1] * j)) >= 0
    ):
        top_value = -1
        k = 0
        while (
            len(data) > (y := lead_y + (exploration_direction[0] * k)) >= 0
            and len(data[-1]) > (x := lead_x + (exploration_direction[1] * k)) >= 0
        ):
            if (d := data[y][x]) > top_value:
                top_value = d
                trees.add((y, x))
            k += 1
        j += 1

print(len(trees))
