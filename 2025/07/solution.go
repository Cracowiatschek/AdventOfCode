package main

import (
	"fmt"
	"os"
	"strconv"
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
	cache := make(map[string]int)
	resultTwo := beamsTrace([]int{0, beams[0][1]}, extractData, cache)

	fmt.Println("Part one: ", result, "\nPart two: ", resultTwo)

}

func beamsTrace(start []int, data []string, c map[string]int) int {
	for {
		next := start
		next[0] = next[0] + 1

		i := strconv.Itoa(start[0])
		j := strconv.Itoa(start[1])
		val := i + "|" + j
		value, ok := c[val]
		if ok {
			return value
		}

		if next[0] >= len(data)-1 {
			c[val] += 1
			return 1
		}

		if data[next[0]][next[1]] == '^' {
			left := []int{next[0], next[1] - 1}
			right := []int{next[0], next[1] + 1}
			result := beamsTrace(left, data, c) + beamsTrace(right, data, c)
			c[val] += result
			return result
		}
	}
}
