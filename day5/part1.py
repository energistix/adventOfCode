import re

lines = []

parameters = set()

with open("./input.txt", "r") as file:
    lines = list(file.readlines())

source = ""
destination = ""


def custom_range(start: int, length: int) -> range:
    return range(start, start + length)


for line in lines:
    match = re.match("(.+)-to-(.+?)\\s", line)
    if match:
        groups = match.groups()
        for group in groups:
            parameters.add(group)
        source = groups[0]
        destination = groups[1]
