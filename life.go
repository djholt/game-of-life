package main

import (
  "fmt"
  "os"
  "os/exec"
  "strconv"
  "strings"
  "time"
)

type Life struct {
  Board map[string]bool
}

func (life *Life) IsAlive(cellKey string) bool {
  return life.Board[cellKey]
}

func (life *Life) BecomeAlive(cellKey string) {
  life.Board[cellKey] = true
}

func (life *Life) Run() {
  for {
    life.PrintBoard()
    time.Sleep(100 * time.Millisecond)
    life.Tick()
  }
}

func (life *Life) PrintBoard() {
  c := exec.Command("clear")
  c.Stdout = os.Stdout
  c.Run()

  for y := 0; y < 30; y++ {
    row := ""

    for x := 0; x < 80; x++ {
      if life.IsAlive(fmt.Sprintf("%d,%d", x, y)) {
        row += "#"
      } else {
        row += "."
      }
    }

    fmt.Println(row)
  }
}

func (life *Life) Tick() {
  newBoard := make(map[string]bool)

  for _, cellKey := range life.CandidateCells() {
    numAlive := life.NumberOfAliveNeighbors(cellKey)

    if life.IsAlive(cellKey) && numAlive == 2 || numAlive == 3 {
      newBoard[cellKey] = true
    }
  }

  life.Board = newBoard
}

func (life *Life) CandidateCells() []string {
  cellKeys := make(map[string]bool)

  for _, cellKey := range keysInMap(life.Board) {
    if life.IsAlive(cellKey) {
      cellKeys[cellKey] = true

      for _, neighborKey := range life.NeighborCells(cellKey) {
        cellKeys[neighborKey] = true
      }
    }
  }

  return keysInMap(cellKeys)
}

func (life *Life) NeighborCells(cellKey string) []string {
  pair := strings.Split(cellKey, ",")
  x, _ := strconv.Atoi(pair[0])
  y, _ := strconv.Atoi(pair[1])

  neighborKeys := make([]string, 8)

  neighborKeys[0] = fmt.Sprintf("%d,%d", x-1, y-1)
  neighborKeys[1] = fmt.Sprintf("%d,%d", x,   y-1)
  neighborKeys[2] = fmt.Sprintf("%d,%d", x+1, y-1)
  neighborKeys[3] = fmt.Sprintf("%d,%d", x-1, y)
  neighborKeys[5] = fmt.Sprintf("%d,%d", x+1, y)
  neighborKeys[4] = fmt.Sprintf("%d,%d", x-1, y+1)
  neighborKeys[6] = fmt.Sprintf("%d,%d", x,   y+1)
  neighborKeys[7] = fmt.Sprintf("%d,%d", x+1, y+1)

  return neighborKeys
}

func (life *Life) NumberOfAliveNeighbors(cellKey string) int {
  count := 0

  for _, neighborKey := range life.NeighborCells(cellKey) {
    if life.IsAlive(neighborKey) {
      count++
    }
  }

  return count
}

func keysInMap(m map[string]bool) []string {
  keys := make([]string, len(m))

  i := 0
  for k, _ := range m {
    keys[i] = k
    i++
  }

  return keys
}

func main() {
  game := Life{Board: make(map[string]bool)}

  game.BecomeAlive("1,5")
  game.BecomeAlive("2,5")
  game.BecomeAlive("1,6")
  game.BecomeAlive("2,6")
  game.BecomeAlive("13,3")
  game.BecomeAlive("14,3")
  game.BecomeAlive("12,4")
  game.BecomeAlive("16,4")
  game.BecomeAlive("11,5")
  game.BecomeAlive("17,5")
  game.BecomeAlive("11,6")
  game.BecomeAlive("15,6")
  game.BecomeAlive("17,6")
  game.BecomeAlive("18,6")
  game.BecomeAlive("11,7")
  game.BecomeAlive("17,7")
  game.BecomeAlive("12,8")
  game.BecomeAlive("16,8")
  game.BecomeAlive("13,9")
  game.BecomeAlive("14,9")
  game.BecomeAlive("25,1")
  game.BecomeAlive("23,2")
  game.BecomeAlive("25,2")
  game.BecomeAlive("21,3")
  game.BecomeAlive("22,3")
  game.BecomeAlive("21,4")
  game.BecomeAlive("22,4")
  game.BecomeAlive("21,5")
  game.BecomeAlive("22,5")
  game.BecomeAlive("23,6")
  game.BecomeAlive("25,6")
  game.BecomeAlive("25,7")
  game.BecomeAlive("35,3")
  game.BecomeAlive("36,3")
  game.BecomeAlive("35,4")
  game.BecomeAlive("36,4")
  game.BecomeAlive("62,6")
  game.BecomeAlive("63,6")
  game.BecomeAlive("64,6")
  game.BecomeAlive("68,6")
  game.BecomeAlive("69,6")
  game.BecomeAlive("70,6")
  game.BecomeAlive("60,8")
  game.BecomeAlive("65,8")
  game.BecomeAlive("67,8")
  game.BecomeAlive("72,8")
  game.BecomeAlive("60,9")
  game.BecomeAlive("65,9")
  game.BecomeAlive("67,9")
  game.BecomeAlive("72,9")
  game.BecomeAlive("60,10")
  game.BecomeAlive("65,10")
  game.BecomeAlive("67,10")
  game.BecomeAlive("72,10")
  game.BecomeAlive("62,11")
  game.BecomeAlive("63,11")
  game.BecomeAlive("64,11")
  game.BecomeAlive("68,11")
  game.BecomeAlive("69,11")
  game.BecomeAlive("70,11")
  game.BecomeAlive("62,13")
  game.BecomeAlive("63,13")
  game.BecomeAlive("64,13")
  game.BecomeAlive("68,13")
  game.BecomeAlive("69,13")
  game.BecomeAlive("70,13")
  game.BecomeAlive("60,14")
  game.BecomeAlive("65,14")
  game.BecomeAlive("67,14")
  game.BecomeAlive("72,14")
  game.BecomeAlive("60,15")
  game.BecomeAlive("65,15")
  game.BecomeAlive("67,15")
  game.BecomeAlive("72,15")
  game.BecomeAlive("60,16")
  game.BecomeAlive("65,16")
  game.BecomeAlive("67,16")
  game.BecomeAlive("72,16")
  game.BecomeAlive("62,18")
  game.BecomeAlive("63,18")
  game.BecomeAlive("64,18")
  game.BecomeAlive("68,18")
  game.BecomeAlive("69,18")
  game.BecomeAlive("70,18")

  game.Run()
}
