from itertools import product

from tqdm import tqdm

with open("./input.txt", "r") as file:
    lines = list(map(lambda s: s.removesuffix("\n"), file.readlines()))


def compute_size_contiguous_groups(line: str):
    res: list[int] = []
    current = 0
    for char in line:
        if char == "#":
            current += 1
        elif current != 0:
            res.append(current)
            current = 0
    if current != 0:
        res.append(current)
    return res


total = 0

for line in tqdm(lines):
    text, nbrs = line.split(" ")
    nbrs = list(map(int, nbrs.split(",")))
    unknowns: list[int] = [i for i, char in enumerate(text) if char == "?"]
    for combination in product([True, False], repeat=len(unknowns)):
        true_unknown = [n for i, n in enumerate(unknowns) if combination[i]]
        new_text = "".join(
            ["#" if i in true_unknown else char for i, char in enumerate(text)]
        )
        new_nbrs = compute_size_contiguous_groups(new_text)
        if all(
            len(new_nbrs) == len(nbrs) and new_nbrs[i] == nbr
            for i, nbr in enumerate(nbrs)
        ):
            total += 1

print(total)
