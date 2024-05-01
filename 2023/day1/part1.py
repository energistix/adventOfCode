total = 0

with open("./input.txt", "r") as f:
    for line in f.readlines():
        first = ""
        last = ""
        for char in line:
            try:
                n = str(int(char))
                if first == "":
                    first = n
                last = n
            except:
                pass
        number = int(first + last)
        total += number

print(total)
