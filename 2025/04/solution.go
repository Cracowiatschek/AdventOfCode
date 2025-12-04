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
	x := buildMatrix(extractData)
	y := searchRolls(x)
	fmt.Println(y)

}

func buildMatrix(input []string) [][]rune {
	matrix := make([][]rune, len(input))
	for i := range matrix {
		matrix[i] = make([]rune, len(input[0]))
	}

	for y, row := range input {

		for x, col := range row {
			matrix[x][y] = col
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

func setupNeighbours(row, col int, matrix [][]rune) int {
	minRow := 0
	maxRow := len(matrix) - 1
	minCol := 0
	maxCol := len(matrix[0]) - 1
	//	fmt.Println(minCol,maxCol, minRow,maxRow, "BEFORE")

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

	matrix = matrix[minRow:maxRow]
	for _, value := range matrix {
		for _, char := range value[minCol:maxCol] {
			if string(char) == "@" {

				result++
			}
		}
	}
	return result
}
