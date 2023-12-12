from __future__ import annotations

with open("./inputText.txt", "r") as file:
    lines = list(map(lambda l: l.removesuffix("\n"), file.readlines()))

seeds = list(map(int, lines.pop(0).removeprefix("seeds: ").split(" ")))
lines.pop(0)


class MyRange:
    def __init__(self, destination: int, source: int, length: int):
        self.destination = destination
        self.source = source
        self.length = length
        self.source_end = source + length
        self.destination_end = destination + length
        self.offset = destination - source

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


class SimpleRange:
    def __init__(self, source: int, end: int):
        self.source = source
        self.end = end

    def hasOverlap(self, other: MyRange) -> bool:
        if (other.source <= self.source and other.source_end >= self.source) or (
            other.source <= self.end and other.source_end >= self.end
        ):
            return True
        return False

    def transform(self, other: MyRange) -> list[SimpleRange]:
        out: list[SimpleRange] = []
        # ma source est au milieu de la source de l'autre
        if other.source < self.source and other.source_end > self.source:
            out.append(SimpleRange(other.source, self.source - 1))
        # ma destination est au milieu de la source de l'autre
        if other.source < self.end and other.source_end > self.end:
            out.append(SimpleRange(other.source_end, self.end))

        out.append(
            SimpleRange(
                max(self.source, other.source) + other.offset,
                min(other.destination, self.end) + other.offset,
            )
        )

        return out

    def __str__(self) -> str:
        return f"SimpleRange({self.source}, {self.end})"


class RangeGroup:
    def __init__(self):
        self.ranges: list[SimpleRange] = []

    def add_range(self, source: int, length: int):
        self.ranges.append(SimpleRange(source, source + length))

    def transform(self, map: MyMap):
        for myRange in map.ranges:
            res: list[SimpleRange] = []

            for simpleRange in self.ranges:
                if simpleRange.hasOverlap(myRange):
                    res.extend(simpleRange.transform(myRange))
                else:
                    res.append(simpleRange)

            self.ranges = res

    def __repr__(self) -> str:
        out = "RangeGroup(\n"
        for range in self.ranges:
            out += str(range) + ",\n"
        out += ")"
        return out


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


seedsRanges = RangeGroup()

for i in range(0, len(seeds), 2):
    seedsRanges.add_range(seeds[i], seeds[i + 1])

print(seedsRanges)

for map in maps:
    seedsRanges.transform(map)
    print(seedsRanges)
