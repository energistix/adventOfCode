with open("./input.txt") as file:
    data = file.read()

i = 14
done = False
while not done:
    if len(set(data[i - 14 : i])) >= 14:
        done = True
    i += 1

print(i - 1)
