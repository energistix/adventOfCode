with open("./input.txt", encoding="utf-8") as file:
    data = file.readlines()

data = map(lambda d: d.split(","), data)
data = map(lambda d: list(map(lambda r: list(map(int, r.split("-"))), d)), data)

result = 0

for d in data:
    if d[0][0] >= d[1][0] and d[0][1] <= d[1][1]:
        result += 1
    elif d[1][0] >= d[0][0] and d[1][1] <= d[0][1]:
        result += 1

print(result)
