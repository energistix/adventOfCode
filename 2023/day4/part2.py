# 1097 too low

lines: list[str] = []

with open("./input.txt", "r") as file:
    lines = list(file.readlines())

ammountOfScratchCards = [1 for _ in range(len(lines))]

for line in lines:
    line = line.removeprefix("Card ")

    currentNumber = ""
    gameId = 0
    for char in line:
        if char.isdigit():
            currentNumber += char
        elif len(currentNumber) > 0:
            gameId = int(currentNumber)
            break

    line = line[5:]

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

    rightNumbersAmmount = 0

    for playedNumber in playedNumbers:
        if playedNumber in winnerNumbers:
            rightNumbersAmmount += 1

    for i in range(1, min(1 + rightNumbersAmmount, len(lines) - 2)):
        ammountOfScratchCards[gameId - 1 + i] += ammountOfScratchCards[gameId - 1]

print(sum(ammountOfScratchCards))
