package main

import (
	"fmt"
	"os"
	//	"strconv"
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
	var beams [][]int
	for i, v := range extractData[0] {
		if v == 'S' {
			beams = append(beams, []int{1, i})
		}
	}
	var splitter [][]int
	result := 0
	for i, row := range extractData {
		for j, col := range row {
			if col == '^' {
				splitter = append(splitter, []int{i, j})
				for _, beam := range beams {
					if beam[0] == i-1 && beam[1] == j {
						result++
						beams = append(beams, []int{i + 1, j - 1}, []int{i + 1, j + 1})
						break

					}
				}
			} else {
				for _, beam := range beams {
					if beam[0] == i-2 && beam[1] == j && extractData[i-1][j] != '^' {
						beams = append(beams, []int{i, j})

					}
				}
			}
		}
	}

	fmt.Println(result, beams) // splitter, beams,

}
