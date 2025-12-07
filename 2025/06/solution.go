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

	var ranges [][]int
	var operators []string
	start := 0
	maxIdx := 0
	operators = append(operators, string(extractData[len(extractData)-1][start]))

	for i := range extractData {
		if len(extractData[i])-1 > maxIdx {
			maxIdx = len(extractData[i]) - 1
		}
	}

	for i := range extractData[len(extractData)-1] {
		if string(extractData[len(extractData)-1][i]) != " " && i != 0 {
			ranges = append(ranges, []int{start, i - 1})
			operators = append(operators, string(extractData[len(extractData)-1][i]))
			start = i
		}
	}
	ranges = append(ranges, []int{start, maxIdx})

	resultOne, resultTwo := calculateSheet(extractData[:len(extractData)-1], operators, ranges)

	fmt.Println("Part one: ", resultOne, "\nPart two: ", resultTwo)
}

func calculateSheet(data, operators []string, ranges [][]int) (int, int) {
	result := 0
	result1 := 0
	lastOperator := false
	for i, operator := range operators {
		var numbers []int
		var raw []string
		if i == len(operators)-1 {
			lastOperator = true
		}
		for _, row := range data {
			if lastOperator {
				ranges[i][1] = len(row)
			}
			raw = append(raw, row[ranges[i][0]:ranges[i][1]])
			textNum := strings.Replace(row[ranges[i][0]:ranges[i][1]], " ", "", -1)
			value, _ := strconv.Atoi(textNum)
			numbers = append(numbers, value)
		}
		pivotNum := pivotNumbers(raw)
		tempResult := 0
		tempResult1 := 0
		if operator == "*" {
			tempResult = 1
			tempResult1 = 1
		}

		for _, num := range numbers {
			if operator == "+" {
				tempResult += num
			} else {
				tempResult *= num
			}
		}
		for _, num := range pivotNum {
			if operator == "+" {
				tempResult1 += num
			} else {
				tempResult1 *= num
			}
		}
		result += tempResult
		result1 += tempResult1
	}
	return result, result1
}

func pivotNumbers(numbers []string) []int {
	var textNumbers []string
	maxId := 0
	for _, val := range numbers {
		if len(val)-1 > maxId {
			maxId = len(val) - 1
		}
	}

	for i := range maxId + 1 {
		var val string
		for _, num := range numbers {
			if i <= len(num)-1 {
				val = val + string(num[i])
			}

		}
		textNumbers = append(textNumbers, val)
	}

	var result []int
	for _, val := range textNumbers {
		val = strings.Replace(val, " ", "", -1)
		valString, _ := strconv.Atoi(val)
		result = append(result, valString)
	}
	return result
}
