numbs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [i + 1 for i in range(9)]
dict1 = dict(zip(numbs, numbers))
dict2 = dict(zip(map(str, numbers), numbers))
dict3 = {**dict1, **dict2}

total = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        first = ""
        last = ""
        for i in range(len(line)):
            for strNumber, number in dict3.items():
                right = True
                for j, char in enumerate(strNumber):
                    if i + j >= len(line) or line[i + j] != char:
                        right = False
                        break
                if right:
                    if first == "":
                        first = str(number)
                    last = str(number)
                    break
        total += int(first + last)

print(total)
