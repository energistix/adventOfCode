import re


def letter_to_number(letter: str) -> int:
    if re.match(r"[a-z]", letter):
        return ord(letter) - 96
    if re.match(r"[A-Z]", letter):
        return ord(letter) - 38
    return 0


with open("./input.txt", encoding="utf-8") as file:
    data = file.readlines()

data = map(lambda d: d[:-1], data)
data = map(lambda d: (d[: (len(d) // 2)], d[(len(d) // 2) :]), data)
data = map(lambda d: set(d[0]) & set(d[1]), data)
data = map(lambda d: letter_to_number(list(d)[0]), data)

print(sum(data))
