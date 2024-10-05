import * as fs from "fs/promises"
import { Board } from "./Board"

const text = await fs.readFile("./input.txt", "utf-8")
const [numbersText, ...boardsText] = text.split("\n\n")
const boards = boardsText
  .map((board) =>
    board.split("\n").map((line) =>
      line
        .split(/\s+/)
        .map((n) => Number.parseInt(n))
        .filter((n) => !Number.isNaN(n))
    )
  )
  .map((b) => new Board(b))

const numbers = numbersText.split(",").map((n) => Number(n))
let lastNumber: number = 0
let currentNumber: number = numbers.shift() ?? -1
if (currentNumber === -1) throw new Error("No numbers ??")

let losingBoard: Board | undefined

while (Board.winningBoards.length !== boards.length) {
  boards.forEach((board) => board.select(currentNumber))
  lastNumber = currentNumber
  currentNumber = numbers.shift() ?? -1
  if (currentNumber === -1) throw new Error("No numbers ??")
  if (Board.winningBoards.length + 1 === boards.length) {
    losingBoard = boards.find((board) => !board.won)
  }
}

console.log(losingBoard)
console.log(losingBoard?.score)
