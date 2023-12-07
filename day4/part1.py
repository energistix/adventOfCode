lines: list[str] = []

with open("./input.txt", "r") as file:
    lines = list(file.readlines())

total = 0

for line in lines:
    line = line.removeprefix("Card")
    line = line[6:]

    winnerNumbers: list[int] = []
    playedNumbers: list[int] = []

    collectingWinningNumbers = True

    currentNumber = ""
    for char in line:
        if char.isdigit():
            currentNumber += char
        elif len(currentNumber) > 0:
            if collectingWinningNumbers:
                winnerNumbers.append(int(currentNumber))
            else:
                playedNumbers.append(int(currentNumber))
            currentNumber = ""
        if char == "|":
            collectingWinningNumbers = False

    rightNumbersAmmount = -1

    for playedNumber in playedNumbers:
        if playedNumber in winnerNumbers:
            rightNumbersAmmount += 1

    if rightNumbersAmmount != -1:
        total += 2**rightNumbersAmmount

print(total)
