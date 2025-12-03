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

	resultOne := 0
	resultTwo := 0

	for _, row := range extractData {
		resultOne += findJoltage(row, 2)
		resultTwo += findJoltage(row, 12)
	}
	fmt.Println("Part one: ", resultOne, "\nPart two: ", resultTwo)
}

func findJoltage(row string, digitLen int) int {
	var digit []string
	toSearch := digitLen
	lastDigit := 0
	lastIdx := 0

	for range digitLen {
		lastDigit = 0
		lastIdx = 0
		for char := range row[:len(row)-toSearch+1] {
			charNum, _ := strconv.Atoi(string(row[char]))
			if charNum > lastDigit {
				lastDigit = charNum
				lastIdx = char

			}
			if charNum == 9 {
				break
			}
		}

		digit = append(digit, strconv.Itoa(lastDigit))
		row = row[lastIdx+1:]
		toSearch--

		if len(row) == toSearch {
			joinDigits := strings.Join(digit, "")
			digitInt, _ := strconv.Atoi(joinDigits + row)
			return digitInt
		}

		if toSearch == 0 {
			joinDigits := strings.Join(digit, "")
			digitInt, _ := strconv.Atoi(joinDigits)
			return digitInt
		}
	}
	return 0
}
