import * as fs from "fs/promises"

const input = await fs.readFile("input.txt", "utf8")
const lines = input.split("\n")

const mostCommonBits = new Array(lines[0].length).fill(0)
lines.forEach((line) => {
  line.split("").forEach((char, i) => {
    mostCommonBits[i] += char === "1" ? 1 : -1
  })
})

const gammaRate = parseInt(mostCommonBits.map((n) => (n > 0 ? 1 : 0)).join(""), 2)
const epsilonRate = parseInt(mostCommonBits.map((n) => (n < 0 ? 1 : 0)).join(""), 2)
console.log(gammaRate)
console.log(epsilonRate)
console.log(gammaRate * epsilonRate)
