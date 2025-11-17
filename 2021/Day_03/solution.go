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

	maxRange := len(extractData)
	positionVal := make([]int, len(extractData[0]))

	for i := range extractData {
		line := strings.Split(extractData[i], "")

		for j := range line {
			value, _ := strconv.Atoi(line[j])
			positionVal[j] += value
		}
	}
	gammaCode := make([]string, len(positionVal))
	epsilonCode := make([]string, len(positionVal))

	for i := range positionVal {
		if positionVal[i] > (maxRange / 2) {
			gammaCode[i] = "1"
			epsilonCode[i] = "0"
		} else {
			gammaCode[i] = "0"
			epsilonCode[i] = "1"
		}
	}

	gammaDecode, _ := strconv.ParseInt(strings.Join(gammaCode, ""), 2, 64)
	epsilonDecode, _ := strconv.ParseInt(strings.Join(epsilonCode, ""), 2, 64)

	fmt.Println("Part One:", gammaDecode*epsilonDecode)

	carbodioxydeBytes := extractData
	oxygenBytes := extractData

	carbodioxyde := make([]string, len(extractData[0]))
	oxygen := make([]string, len(extractData[0]))

	one := 0
	zero := 0

	for i := range len(extractData[0]) {
		one = 0
		zero = 0
		for j := range len(carbodioxydeBytes) {
			byteStr := strings.Split(carbodioxydeBytes[j], "")
			if byteStr[i] == "1" {
				one += 1
			} else {
				zero += 1
			}
		}

		if one >= zero {
			var result []string

			for j := range len(carbodioxydeBytes) {
				byteStr := strings.Split(carbodioxydeBytes[j], "")
				if byteStr[i] == "1" {
					result = append(result, carbodioxydeBytes[j])
				}
			}
			carbodioxydeBytes = result
			carbodioxyde = append(carbodioxyde, "1")
		}
		if one < zero {
			var result []string

			for j := range len(carbodioxydeBytes) {
				byteStr := strings.Split(carbodioxydeBytes[j], "")
				if byteStr[i] == "0" {
					result = append(result, carbodioxydeBytes[j])
				}
			}
			carbodioxydeBytes = result
			carbodioxyde = append(carbodioxyde, "0")
		}
	}

	for i := range len(extractData[0]) {
		one = 0
		zero = 0
		for j := range len(oxygenBytes) {
			byteStr := strings.Split(oxygenBytes[j], "")
			if byteStr[i] == "1" {
				one += 1
			} else {
				zero += 1
			}
		}
		if one+zero > 1 {
			if one >= zero {
				var result []string

				for j := range len(oxygenBytes) {
					byteStr := strings.Split(oxygenBytes[j], "")
					if byteStr[i] == "0" {
						result = append(result, oxygenBytes[j])
					}
				}
				oxygenBytes = result
				oxygen = append(oxygen, "0")
			}
			if one < zero {
				var result []string

				for j := range len(oxygenBytes) {
					byteStr := strings.Split(oxygenBytes[j], "")
					if byteStr[i] == "1" {
						result = append(result, oxygenBytes[j])
					}
				}
				oxygenBytes = result
				oxygen = append(oxygen, "1")
			}
			if one == 0 && zero == 0 {
				oxygen = append(oxygen, "0")
			}
		} else {
			if one == 1 {
				oxygen = append(oxygen, "1")
			}
			if zero == 1 {
				oxygen = append(oxygen, "0")
			}
		}
	}

	carbodioxydeDecode, _ := strconv.ParseInt(strings.Join(carbodioxyde, ""), 2, 64)
	oxygenDecode, _ := strconv.ParseInt(strings.Join(oxygen, ""), 2, 64)

	fmt.Println("Part Two:", carbodioxydeDecode*oxygenDecode)
}
