with open("./input.txt") as file:
    lines = list(map(lambda l: l.removesuffix("\n"), file.readlines()))

seeds = lines.pop(0).removeprefix("seeds: ").split(" ")
lines.pop(0)


class MyRange:
    def __init__(self, destination: int, source: int, length: int):
        self.destination = destination
        self.source = source
        self.length = length

    def is_in_source(self, n: int) -> bool:
        if n >= self.source and n <= self.source + self.length:
            return True
        return False

    def value(self, n: int) -> int:
        if not self.is_in_source(n):
            raise ValueError(f"{n} is not in range {self}")
        index = n - self.source
        return self.destination + index

    def __repr__(self) -> str:
        return f"Range({self.destination}, {self.source}, {self.length})"


class MyMap:
    def __init__(self):
        self.ranges: list[MyRange] = []

    def value(self, n: int) -> int:
        for range in self.ranges:
            if range.is_in_source(n):
                return range.value(n)
        return n

    def add_range(self, destination: int, source: int, length: int):
        self.ranges.append(MyRange(destination, source, length))


mapsAmmount = 7
maps: list[MyMap] = []

for _ in range(mapsAmmount):
    lines.pop(0)
    current_map = MyMap()
    maps.append(current_map)
    line = lines.pop(0)
    while line != "":
        nbrs = map(int, line.split(" "))
        current_map.add_range(*nbrs)
        if len(lines) > 0:
            line = lines.pop(0)
        else:
            line = ""

results: list[int] = []

for seed in seeds:
    value = int(seed)
    for map in maps:
        value = map.value(value)
    results.append(value)

print(min(results))
