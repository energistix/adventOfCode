import re
from functools import reduce
from itertools import groupby


def letter_to_number(letter: str) -> int:
    if re.match(r"[a-z]", letter):
        return ord(letter) - 96
    if re.match(r"[A-Z]", letter):
        return ord(letter) - 38
    return 0


with open("./input.txt", encoding="utf-8") as file:
    data = file.readlines()

data = map(lambda d: d[:-1], data)
data = map(set, data)

i = -1


def key(_):
    global i
    i += 1
    return i // 3


data = groupby(list(data), key)
data = map(lambda d: d[1], data)
data = map(lambda d: reduce(lambda a, b: a & b, d), data)
data = map(lambda d: letter_to_number(list(d)[0]), data)


print(sum(data))
