package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Field struct {
	Value string
	X int
	Y int
}

type Board struct {
	Fields []Field
	LastCall int
	IsWin bool
	rowCache []int
	columnCache []int
}

func Counter[T comparable](slice []T) map[T]int {
    m := make(map[T]int)
    for _, v := range slice {
        m[v]++
    }
    return m
}

func (b *Board) CacheAndCheck (x int, y int) {
	b.rowCache = append(b.rowCache, x)
	b.columnCache = append(b.columnCache, y)

	cntRow := Counter(b.rowCache)
	cntCol := Counter(b.columnCache)
	for i := range(len(cntRow)) {
		fmt.Println(cntRow[i], cntRow)
		if cntRow[i] == 5 {
			b.IsWin = true
		}
	}

	for i := range(len(cntCol)) {
		if cntCol[i] == 5 {
			b.IsWin = true
		}
	}
}

func main() {
	file := os.Args[1]

	raw, err := os.ReadFile(file)
	if err != nil {
		fmt.Println(err)
	}

	stringData := string(raw)
	extractData := strings.Split(stringData, "\n")

	numbers := strings.Split(extractData[0], ",")

	var boards []Board
	var fields []Field

	x := 0
	y := 0

	for i := range(len(extractData[2:])) {
		row := strings.Split(extractData[i+2], " ")
		for j := range(len(row)) {
			if len(row[j]) != 0 {
				fields = append(fields, Field{row[j], i,j})
				y+=1
			}
		}
		y=0
		x+=1
		if len(row) == 1 {
			x=0
			boards = append(boards, Board{fields, 0, false, []int{}, []int{}})
			fields = []Field{}
		}
	}
	boards = append(boards, Board{fields, 0, false,[]int{}, []int{}})

	fmt.Println(numbers)
	call := 0

	for i := range(len(numbers)) {
		call += 1
		for j := range(len(boards)) {
			for h := range(len(boards[j].Fields)) {
				if boards[j].Fields[h].Value == numbers[i] {
					boards[j].LastCall,_  = strconv.Atoi(numbers[i])
					boards[j].CacheAndCheck(boards[j].Fields[h].X, boards[j].Fields[h].Y)
					fmt.Println(boards[j].columnCache, boards[j].rowCache,)
					if boards[j].IsWin {
						fmt.Println("OK", call, numbers[call-1])
						break
					}
				}
			}
		}
	}
	fmt.Println(call, numbers[call-1])
}



