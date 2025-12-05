
package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
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
				ranges = append(ranges, []int{to,from})
			} else {
				ranges = append(ranges, []int{from,to})
			}

		}
	}

	num := getNumberInRange(numbers,ranges)
	rng := getCorrectRanges(num,ranges)
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

	result := 0
	var cache [][]int
	for _, num := range numbers {
		for _, rng := range ranges {
			if num >= rng[0] && num <= rng[1] {
				cache = append(cache, rng)
			}
		}
	}
	cache = sort(cache)
	
	var correctRanges [][]int
	for {
		isCompleted := true
		for _, val := range cache {
			minVal := val[0]
			maxVal := val[1]
			if len(correctRanges) > 0 {
				toBreak := false
				for _, rng := range correctRanges {
					if minVal >= rng[0] && maxVal <= rng[1] {
						toBreak =true
						break
					}
				}
				if toBreak {
					break
				}
			}
			for _, search := range cache {
				if search[0] <= maxVal && search[1] >= maxVal && search[0] >= minVal {
					maxVal = search[1]
					isCompleted = false
				}
				if search[0] < minVal && search[1] <= maxVal && search[1] >= minVal {
					minVal = search[0]
					isCompleted = false
				}
				if search[0] <= minVal && search[1] >= maxVal {
					minVal = search[0]
					maxVal = search[1]
					isCompleted = false
				}

			}
			correctRanges = append(correctRanges, []int{minVal,maxVal})

		}
		if isCompleted {
			break
		}
	}
	fmt.Println(correctRanges)
	for _, rng := range correctRanges {
		result += rng[1]-rng[0]+1
	}

	return result
}

func sort(list [][]int) [][]int {
	for {
		isSorted := true
		for i := range list {
			if i + 1 > len(list)-1 {
				break
			}
			if list[i][1] > list[i+1][1] {
				a:= list[i]
				b:=list[i+1]
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