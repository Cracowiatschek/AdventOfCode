package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
//	"sort"
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
		resultOne += findJoltage(row)
		resultTwo += findMoreJoltage(row)

	}
	fmt.Println(resultOne, resultTwo)
}

func findJoltage(row string) int {
//	textLen := len(row)
	firstDigit := 0
	firstDigitIdx := 0
	secondDigit := 0
	firstIsSecond := false
	for char :=range row {
		charNum,_ := strconv.Atoi(string(row[char]))
		if charNum > firstDigit {
			firstDigit = charNum
			firstDigitIdx = char
		}
		if charNum == 9 {
			break
		}
	}
	if firstDigitIdx == len(row)-1 {
		row = row[:firstDigitIdx]
		firstIsSecond = true
	} else {
		row = row[firstDigitIdx+1:]
	}
	for char :=range row {
		charNum,_ := strconv.Atoi(string(row[char]))
		if charNum > secondDigit {
			secondDigit = charNum
		}
	}
	charFirstDigit := strconv.Itoa(firstDigit)
	charSecondDigit := strconv.Itoa(secondDigit)
	result := 0
	if firstIsSecond {
		result, _ = strconv.Atoi(charSecondDigit+charFirstDigit)
	} else {
		result, _ = strconv.Atoi(charFirstDigit+charSecondDigit)
	}
	return result
}


