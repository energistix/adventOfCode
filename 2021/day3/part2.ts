import * as fs from "fs/promises"

const input = await fs.readFile("input.txt", "utf8")
const lines = input.split("\n")

function findMostCommonBitsIndex(lines: string[]) {
  const mostCommonBits = new Array(lines[0].length).fill(0)
  lines.forEach((line) => {
    line.split("").forEach((char, i) => {
      mostCommonBits[i] += char === "1" ? 1 : -1
    })
  })
  return mostCommonBits
}

const mostCommonBits = findMostCommonBitsIndex(lines)

let O2Values = lines
let i = 0
while (O2Values.length > 1) {
  const index = findMostCommonBitsIndex(O2Values)
  O2Values = O2Values.filter((value) => {
    if (index[i] === 0) return value[i] === "1"
    return value[i] === (index[i] > 0 ? "1" : "0")
  })
  i++
}
const O2 = parseInt(O2Values[0], 2)
console.log(O2)

let CO2Values = lines
i = 0
while (CO2Values.length > 1) {
  const index = findMostCommonBitsIndex(CO2Values)
  CO2Values = CO2Values.filter((value) => {
    if (index[i] === 0) return value[i] === "0"
    return value[i] === (index[i] < 0 ? "1" : "0")
  })
  i++
}
const CO2 = parseInt(CO2Values[0], 2)
console.log(CO2)

console.log(CO2 * O2)
