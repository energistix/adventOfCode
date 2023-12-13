from functools import cmp_to_key


def parseHand(hand: str) -> int:
    ammounts: dict[str, int] = {}

    for char in hand:
        ammounts[char] = ammounts.get(char, 0) + 1

    highestAmmountChar = ""
    highestAmountValue = 0
    for char, value in ammounts.items():
        if highestAmmountChar == "" and char != "J":
            highestAmmountChar = char
            highestAmountValue = value
        elif value > highestAmountValue and char != "J":
            highestAmmountChar = char
            highestAmountValue = value

    if "J" in ammounts:
        if highestAmmountChar != "":
            ammounts[highestAmmountChar] += ammounts["J"]
        else:
            ammounts["K"] = ammounts["J"]
        ammounts["J"] = 0

    for char, ammount in ammounts.items():
        if ammount == 2:
            for other_char, other_ammount in ammounts.items():
                if other_char != char:
                    if other_ammount == 3:
                        return 5
                    elif other_ammount == 2:
                        return 3
            return 2
        elif ammount == 3:
            for other_char, other_ammount in ammounts.items():
                if other_char != char and other_ammount == 2:
                    return 5
            return 4
        elif ammount == 4:
            return 6
        elif ammount == 5:
            return 7
    return 1


cardsInOrder = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def compareHandByCards(hand1: str, hand2: str) -> int:
    for i in range(len(hand1)):
        char1Value = cardsInOrder.index(hand1[i])
        char2Value = cardsInOrder.index(hand2[i])
        if char1Value < char2Value:
            return 1
        elif char2Value < char1Value:
            return -1
    return 1


def compareHands(hand1: str, hand2: str) -> int:
    res = parseHand(hand1) - parseHand(hand2)
    return res if res != 0 else compareHandByCards(hand1, hand2)


lines = []
with open("./input.txt", "r") as file:
    lines = list(file.readlines())

hands: list[tuple[str, int]] = []
for line in lines:
    hand, bid = line.split(" ")
    hands.append((hand, int(bid)))


def customCompare(hand1: tuple[str, int], hand2: tuple[str, int]):
    return compareHands(hand1[0], hand2[0])


hands.sort(key=cmp_to_key(customCompare))

total = sum((i + 1) * hand[1] for i, hand in enumerate(hands))
print(total)
