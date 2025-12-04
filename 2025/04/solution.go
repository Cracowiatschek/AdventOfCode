package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	file := os.Args[1]
	raw, err := os.ReadFile(file)
	if err != nil {
		fmt.Println(err)
	}
	stringData := string(raw)
	extractData := strings.Split(stringData, "\n")
	array := buildMatrix(extractData)
	resultOne := searchRolls(array)
	resultTwo := removeRolls(array)
	fmt.Println("Part one: ", resultOne, "\nPart two: ", resultTwo)

}

func buildMatrix(input []string) [][]rune {
	matrix := make([][]rune, len(input))
	for i := range matrix {
		matrix[i] = make([]rune, len(input[0]))
	}

	for y, row := range input {

		for x, col := range row {
			matrix[y][x] = col
		}
	}
	return matrix
}

func searchRolls(matrix [][]rune) int {
	rolls := 0

	for i := range matrix {
		for j, col := range matrix[i] {
			if col == '@' {
				if setupNeighbours(i, j, matrix) < 4 {
					rolls++
				}
			}
		}
	}
	return rolls
}

func removeRolls(matrix [][]rune) int {
	rolls := 0

	for {
		lastRound := true
		var cache [][]int
		for i := range matrix {
			for j, col := range matrix[i] {
				if col == '@' {
					if setupNeighbours(i, j, matrix) < 4 {
						rolls++
						cache = append(cache, []int{i, j})
						lastRound = false
					}
				}
			}
		}
		for _, val := range cache {
			matrix[val[0]][val[1]] = '.'
		}
		if lastRound {
			break
		}
	}
	return rolls
}

func setupNeighbours(row, col int, matrix [][]rune) int {
	minRow := 0
	maxRow := len(matrix) - 1
	minCol := 0
	maxCol := len(matrix[0]) - 1

	if maxRow > row {
		maxRow = row + 1
	}
	if minRow < row {
		minRow = row - 1
	}
	if maxCol > col {
		maxCol = col + 1
	}
	if minCol < col {
		minCol = col - 1
	}
	result := -1

	for i := range matrix {
		if i >= minRow && i <= maxRow {
			for j := range matrix[i] {
				if j >= minCol && j <= maxCol {
					if matrix[i][j] == '@' {
						result++
					}
				}
			}
		}
	}

	return result
}
