import re

import tqdm

with open("./input.txt", "r") as file:
    timeString = file.readline().removeprefix("Time:")
    total_time = int(re.sub("\\s+", "", timeString))

    distanceString = file.readline().removeprefix("Distance:")
    distance = int(re.sub("\\s+", "", distanceString))

total = 0

for current_time in tqdm.tqdm(range(1, total_time + 1)):
    if current_time * (total_time - current_time) > distance:
        total += 1

print(total)
