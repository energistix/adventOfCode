export class Board {
  private cols: number[][]
  private numbers: number[] = []
  private selectedNumbers: number[] = []
  private amountSelectedInLines: number[]
  private amountSelectedInCols: number[]
  private size: number
  private lastNumber: number
  private static allBoards: Board[] = []

  constructor(private lines: number[][]) {
    const n: number = lines.length
    this.cols = new Array(n).fill(null).map(() => [])
    lines.forEach((line) =>
      line.forEach((n, i) => {
        this.cols[i].push(n)
        this.numbers.push(n)
      })
    )

    this.amountSelectedInCols = new Array(n).fill(0)
    this.amountSelectedInLines = new Array(n).fill(0)
    this.size = n
    Board.allBoards.push(this)
  }

  select(n: number) {
    if (this.numbers.includes(n)) {
      this.selectedNumbers.push(n)
    }
    let lineIndex = this.lines.findIndex((lines) => lines.includes(n))
    if (lineIndex !== -1) {
      this.amountSelectedInLines[lineIndex]++
    }

    let colIndex = this.cols.findIndex((col) => col.includes(n))
    if (colIndex !== -1) {
      this.amountSelectedInCols[colIndex]++
    }

    this.lastNumber = n
  }

  get won() {
    if (this.amountSelectedInCols.some((n) => n === this.size)) return true
    if (this.amountSelectedInLines.some((n) => n === this.size)) return true

    return false
  }

  get unselectedNumbers() {
    return this.numbers.filter((number) => !this.selectedNumbers.includes(number))
  }

  get score() {
    return this.unselectedNumbers.reduce((a, b) => a + b, 0) * this.lastNumber
  }

  static get winningBoards() {
    return Board.allBoards.filter((board) => board.won)
  }
}
