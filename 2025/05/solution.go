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
	var numbers []int
	toNum := false

	for _, line := range extractData {
		if line == "" {
			toNum = true
		}
		if toNum {
			number, _ := strconv.Atoi(line)
			numbers = append(numbers, number)
		} else {
			from, _ := strconv.Atoi(strings.Split(line, "-")[0])
			to, _ := strconv.Atoi(strings.Split(line, "-")[1])
			if to <= from {
				ranges = append(ranges, []int{to, from})
			} else {
				ranges = append(ranges, []int{from, to})
			}

		}
	}

	num := getNumberInRange(numbers, ranges)
	rng := getCorrectRanges(num, ranges)
	fmt.Println(len(num), rng)

}

func getNumberInRange(numbers []int, ranges [][]int) []int {

	var result []int
	for _, num := range numbers {
		for _, rng := range ranges {
			if num >= rng[0] && num <= rng[1] {
				result = append(result, num)
				break
			}
		}
	}
	return result
}
func getCorrectRanges(numbers []int, ranges [][]int) int {
	var finalRanges [][]int
	for _, num := range numbers {
		for idx , rng := range ranges{
			if num >= rng[0] && num <= rng[1] {
				maxIdx := len(ranges)-1
				if idx+1 < maxIdx {
					maxIdx = idx+1
				}
				finalRanges = append(finalRanges, []int{rng[0], rng[1]})
				ranges = append(ranges[:idx], ranges[maxIdx:]...)
			}
		}
	}
	result := 0
	ranges = sort(finalRanges)

	maxVal := ranges[0][1]
	minVal := ranges[0][0]

	for _, rng := range ranges {
		if rng[0] <= maxVal && rng[1] > maxVal {
			maxVal = rng[1]
		} else if rng[0] > maxVal {
			result += maxVal - minVal + 1
			maxVal = rng[1]
			minVal = rng[0]
		}
	}
	result += maxVal - minVal + 1

	return result
}

func sort(list [][]int) [][]int {
	for {
		isSorted := true
		for i := range list {
			if i+1 > len(list)-1 {
				break
			}
			if list[i][0] > list[i+1][0] {
				a := list[i]
				b := list[i+1]
				list[i+1] = a
				list[i] = b
				isSorted = false
			}
		}
		if isSorted {
			break
		}
	}
	return list
}
