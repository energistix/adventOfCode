with open("./input.txt", encoding="utf-8") as file:
    lines = file.readlines()

data = map(lambda d: d.split(","), lines)
data = map(lambda d: list(map(lambda r: list(map(int, r.split("-"))), d)), data)
data = list(data)

result = 0


def do_overlap(x1, x2, y1, y2):
    if x1 >= x2 and y1 >= y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    return x1 <= y2 and y1 <= x2


for d in data:
    if do_overlap(d[0][0], d[0][1], d[1][0], d[1][1]):
        result += 1

print(result)
