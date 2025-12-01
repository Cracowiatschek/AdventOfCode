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

	position := 50
	zeroPositionState := 0
	zeroBreakepoints := 0

	for i := range len(extractData) {
		operation := extractData[i]
		direction := operation[0]
		value, _ := strconv.Atoi(operation[1:])

		pos, breakpointsCount := rotate(direction, value, position)
		position = pos
		if position == 0 {
			zeroPositionState++
			breakpointsCount++
		}
		zeroBreakepoints += breakpointsCount
	}
	fmt.Println("Part one: ", zeroPositionState)
	fmt.Println("Part two: ", zeroBreakepoints)
}

func rotate(direction uint8, value, position int) (int, int) {
	start := position
	breakpointCount := value / 100
	value = value % 100
	rangeMax := 99
	rangeMin := 0

	if direction == 'R' {
		position += value
		if position > rangeMax {
			position = rangeMin + (position - rangeMax - 1)
			if position != 0 && start != 0 {
				breakpointCount++
			}
		}
	}

	if direction == 'L' {
		position -= value
		if position < rangeMin {
			position = rangeMax - (position*(-1) - 1)
			if position != 0 && start != 0 {
				breakpointCount++
			}
		}
	}

//	if breakpointCount > 0 && start == 0 {
//		breakpointCount--
//	}
//
//	if breakpointCount < 0 {
//		breakpointCount = 0
//	}

	return position, breakpointCount
}