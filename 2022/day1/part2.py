with open("./input.txt") as file:
    data = file.read().splitlines()

data = "\n".join(data).split("\n\n")
data = list(map(lambda x:sum(map(int, x)), map(lambda x:x.split("\n"), data)))
data.sort()
print(sum(data[-3:]))
