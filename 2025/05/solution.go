package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sort"
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
	rng := getCorrectRanges(ranges)
	fmt.Println("Part one: ",len(num),"\nPart two: ", rng)

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

func getCorrectRanges( ranges [][]int) int {

	sort.Slice(ranges, func(i, j int) bool {
		return ranges[i][0] < ranges[j][0]
	})

	finalRanges := [][]int{ranges[0]}

	for _, rng :=range ranges[1:] {
		if rng[0] <= finalRanges[len(finalRanges)-1][1]+1 {
			finalRanges[len(finalRanges)-1][1] = max(rng[1], finalRanges[len(finalRanges)-1][1])
		} else {
			finalRanges = append(finalRanges, rng)
		}
	}
	result := 0
	for _, rng := range finalRanges {
		result += (rng[1] - rng[0] + 1)
	}
	return result
}
