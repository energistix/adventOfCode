import re

times = []
distances = []

with open("./input.txt", "r") as file:
    timesString = file.readline().removeprefix("Time:")
    times = list(map(int, [nbr for nbr in re.split("\\s+", timesString) if nbr != ""]))

    distancesString = file.readline().removeprefix("Distance:")
    distances = list(
        map(int, [nbr for nbr in re.split("\\s+", distancesString) if nbr != ""])
    )

total = 1

for i, time in enumerate(times):
    count = 0
    for current_time in range(1, time + 1):
        if current_time * (time - current_time) > distances[i]:
            count += 1
    total *= count

print(total)
