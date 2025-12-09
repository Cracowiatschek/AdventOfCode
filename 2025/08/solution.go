package main

import (
	"fmt"
	"math"
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

	var points []Point
	for _, val := range extractData {
		x, _ := strconv.Atoi(strings.Split(val, ",")[0])
		y, _ := strconv.Atoi(strings.Split(val, ",")[1])
		z, _ := strconv.Atoi(strings.Split(val, ",")[2])
		points = append(points, Point{x, y, z})
		//		fmt.Println(x, y, z)
	}
	cache := make(map[Link]float64)
	for _, val := range points {
		var connected []Point
		var connection []int

		result := searchConnection(val, points, connected, cache, connection)
		fmt.Println(result)
	}

}

type Point struct {
	X int
	Y int
	Z int
}
type Link struct {
	X Point
	Y Point
}

func searchConnection(point Point, allPoints, connected []Point, cache map[Link]float64, connection []int) []int {
	for {
		cleanup := false
		next := point
		connected = append(connected, next)
		counter := make(map[Point]int)

		for _, p := range connected {
			counter[p] += 1
//			fmt.Println(counter)
			if counter[p] >= 2 {
				cleanup = true
				break
			}

		}

		if cleanup {
			for _, p := range connected {
				for i, p2 := range allPoints {
					if p == p2 {
						if len(allPoints)-1 > i+1 {
							allPoints = append(allPoints[:i], allPoints[i+1:]...)
						} else {
							allPoints = allPoints[:i]
						}
					}

				}
			}
			connection = append(connection, len(connected))
			connected = []Point{}
			if len(allPoints) > 0 {
				next = allPoints[0]
				connected = append(connected, next)
			}
		}

		if len(allPoints) > 0 {
			var distance float64
			var lastPoint Point
			isFirstLap := true
			disabled1 := connected[len(connected)-1]
			disabled2 := connected[len(connected)-1]
			if len(connected) > 1 {
				disabled2 = connected[len(connected)-2]
			}
			for _, p := range allPoints {
				if p != disabled1 && p != disabled2 {
					newDistance := 0.0
					l1, l2 := Link{next, p}, Link{p, next}
					v1, v2 := cache[l1], cache[l2]
					if v1 > 0 || v2 > 0 {
						newDistance = max(v1, v2)
					} else {
						newDistance = getDistance(next, p)
						cache[Link{next, p}] = newDistance
					}
					if newDistance < distance && !isFirstLap {
						distance = newDistance
						lastPoint = p
					} else if isFirstLap {
						distance = newDistance
						lastPoint = p
						isFirstLap = false
					}
					//					fmt.Println(next, p, newDistance, distance)
				}

			}

			//			fmt.Println(next, lastPoint, connected, distance, connection)
			return searchConnection(lastPoint, allPoints, connected, cache, connection)
		} else {
			fmt.Println(connected, connection, allPoints)
			return connection
		}

	}
}

func getDistance(point1, point2 Point) float64 {
	sqrt := math.Sqrt(math.Pow(float64(point2.X)-float64(point1.X), 2) + math.Pow(float64(point2.Y)-float64(point1.Y), 2) + math.Pow(float64(point2.Z)-float64(point1.Z), 2))
	return sqrt
}
