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

	horizontal := 0
	depth := 0

	for i := 0; i < len(extractData); i++ {
		operation, valueStr := strings.Split(extractData[i], " ")[0], strings.Split(extractData[i], " ")[1]
		value, _ := strconv.Atoi(valueStr)

		if operation == "forward" {
			horizontal += value
		} else if operation == "up" {
			depth -= value
		} else if operation == "down" {
			depth += value
		} else {
			panic("Unknown operation")
		}
	}

	fmt.Println("Part one: ", horizontal*depth)

	horizontal = 0
	depth = 0
	aim := 0

	for i := 0; i < len(extractData); i++ {
		operation, valueStr := strings.Split(extractData[i], " ")[0], strings.Split(extractData[i], " ")[1]
		value, _ := strconv.Atoi(valueStr)

		if operation == "forward" {
			horizontal += value
			depth += value * aim
		} else if operation == "up" {
			aim -= value
		} else if operation == "down" {
			aim += value
		} else {
			panic("Unknown operation")
		}
	}

	fmt.Println("Part two: ", horizontal*depth)
}
