from typing import Iterable


values = {
    "A":3,
    "B":2,
    "C":1,
    "X":1,
    "Y":2,
    "Z":3
}

with open("./input.txt" ) as file:
    data = file.readlines()

data = map(lambda d:d[:3].split(" "), data)
data = map(lambda d:map(lambda x:values[x], d), data)

wins = ["32","23","11"]


def treatValue(data: Iterable[int]):
    p1, p2 = data
    if p1+p2 == 4:
        return p2+3
    if str(p1)+str(p2) in wins:
        return p2 + 6
    return p2


data = map(treatValue, data)
print(sum(data))
