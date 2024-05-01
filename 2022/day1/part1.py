with open("./input.txt") as file:
    data = file.read().splitlines()

data = "\n".join(data).split("\n\n")
print(max(map(lambda x:sum(map(int, x)), map(lambda x:x.split("\n"), data))))
