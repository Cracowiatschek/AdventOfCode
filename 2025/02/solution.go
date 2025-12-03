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
	extractData := strings.Split(stringData, ",")

	resultSimple := 0
	resultAdvanced := 0

	for i := range len(extractData) {
		a, _ := strconv.Atoi(strings.Split(extractData[i], "-")[0])
		b, _ := strconv.Atoi(strings.Split(extractData[i], "-")[1])
		searchResult := searchRange(a, b)
		advancedSearchResult := advancedSearchRange(a, b)
		resultSimple += sumIntSlice(searchResult)
		resultAdvanced += sumIntSlice(advancedSearchResult)
	}
	fmt.Println("Part one: ", resultSimple, "\nPart two: ", resultAdvanced)
}

func searchRange(a, b int) []int {
	var result []int

	for i := a; i <= b; i++ {

		stringNum := strconv.Itoa(i)
		if findAloneDigit(stringNum) != true {
			if len(stringNum)%2 != 0 {
				stringNum = nextEvenLengthNum(stringNum)
				i, _ = strconv.Atoi(stringNum)
			}

			if i <= b {
				textLen := len(stringNum)
				if stringNum[0:textLen/2] == stringNum[textLen/2:] {
					result = append(result, i)
				}
			}
		}
	}
	return result
}

func advancedSearchRange(a, b int) []int {
	var result []int
	for i := a; i <= b; i++ {
		stringNum := strconv.Itoa(i)
		if findAloneDigit(stringNum) != true {
			textLen := len(stringNum)

			if i <= b {
				for divider := 1; divider < textLen; divider++ {
					if textLen%divider == 0 {
						sliceCount := textLen / divider
						sliceRange := textLen / sliceCount
						firstSlice := stringNum[0:sliceRange]
						isCorrect := true
						startIndex := 0
						endIndex := startIndex + sliceRange
						for range sliceCount - 1 {
							startIndex += sliceRange
							endIndex += sliceRange
							if firstSlice != stringNum[startIndex:endIndex] {
								isCorrect = false
							}
						}
						if isCorrect {
							result = append(result, i)
							break
						}
					}
				}
			}
		}
	}
	return result
}

func nextEvenLengthNum(a string) string {
	if len(a)%2 != 0 {
		return "1" + strings.Repeat("0", len(a))
	} else {
		return a
	}
}

func sumIntSlice(a []int) int {
	result := 0
	for _, i := range a {
		result += i
	}
	return result
}

func findAloneDigit(number string) bool {
	count := make(map[rune]int)

	for _, char := range number {
		count[char]++
	}
	for _, char := range count {
		if char == 1 {
			return true
		}
	}
	return false
}
