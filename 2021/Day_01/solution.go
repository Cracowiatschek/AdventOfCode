package main

import (
	"fmt"
	"strconv"
	"strings"
	"os"
)

func main() {

	file := os.Args[1]

	raw, err := os.ReadFile(file)
	if err != nil {
		fmt.Println(err)
	}

	stringData := string(raw)
	extractData := strings.Split(stringData, "\n")

	measurements := make([]int, len(extractData))

	for i := range len(extractData) {
		val, _ := strconv.Atoi(extractData[i])
		measurements[i] = val
	}

	increased := 0

	for i := 1; i < len(measurements); i++ {
		if measurements[i-1] < measurements[i] {
			increased++
		}
	}

	fmt.Println("Part one:", increased)

	var vals []int

	for i := 0; i < len(measurements); i++ {
		if i == 0 {
			vals = append(vals, measurements[i])
		} else if i == 1 {
			vals[i-1] += measurements[i]
			vals = append(vals, measurements[i])
		} else {
			vals[i-2] += measurements[i]
			vals[i-1] += measurements[i]
			vals = append(vals, measurements[i])
		}
	}

	vals = vals[0 : len(vals)-2]
	increased = 0

	for i := 1; i < len(vals); i++ {
		if vals[i-1] < vals[i] {
			increased++
		}
	}

	fmt.Println("Part two:", increased)
}
