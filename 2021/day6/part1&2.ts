import fs from "fs/promises"

const text = await fs.readFile("./input.txt", "utf-8")

let fishMap = new Map<number, number>()

text
  .split(",")
  .map((n) => Number(n))
  .forEach((n) => {
    fishMap.set(n, (fishMap.get(n) ?? 0) + 1)
  })

const days = 256

for (let day = 0; day < days; day++) {
  const newFishMap: typeof fishMap = new Map()

  newFishMap.set(6, fishMap.get(0) ?? 0)
  newFishMap.set(8, fishMap.get(0) ?? 0)

  for (let i = 1; i <= 8; i++) {
    newFishMap.set(i - 1, (newFishMap.get(i - 1) ?? 0) + (fishMap.get(i) ?? 0))
  }

  fishMap = newFishMap
}

console.log(Array.from(fishMap.values()).reduce((a, b) => a + b))
