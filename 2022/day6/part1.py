with open("./input.txt") as file:
    data = file.read()

i = 4
done = False
while not done:
    if len(set(data[i - 4 : i])) >= 4:
        done = True
    i += 1

print(i - 1)
