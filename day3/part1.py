lines = []

with open("./input.txt") as file:
    lines = list(file.readlines())

skippedNumbers: list[str] = []

total = 0

for i, line in enumerate(lines):
    currentNumber = ""
    isPartNumber = False
    for j, char in enumerate(line):
        if char.isdigit():
            currentNumber += char
            for x in range(-1, 2):
                for y in range(-1, 2):
                    try:
                        offcet_char = lines[i + y][j + x]
                        if (
                            not offcet_char.isdigit()
                            and offcet_char != "."
                            and i + y > 0
                            and j + x > 0
                        ):
                            isPartNumber = True
                    except:
                        pass
        elif len(currentNumber) > 0:
            if isPartNumber:
                total += int(currentNumber)
            currentNumber = ""
            isPartNumber = False
    if isPartNumber:
        total += int(currentNumber)
    currentNumber = ""
    isPartNumber = False


print(total)

with open("./skippedNumbers.txt", "w") as file:
    file.writelines(skippedNumbers)
