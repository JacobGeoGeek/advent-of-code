package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

type NumberPosition struct {
	row int
	col int
}

func part1() {
	file, err := os.Open("./input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	engine := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		engine = append(engine, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	numbersPosition := []NumberPosition{}
	total := 0

	for row, ligne := range engine {
		for col, char := range ligne {
			_, err := strconv.Atoi(string(char))

			if err == nil {
				numbersPosition = append(numbersPosition, NumberPosition{row, col})
			} else {
				isNumberAdjacentToSymbol := false

				for _, number := range numbersPosition {
					topChar := "."
					topLeftChar := "."
					leftChar := "."
					bottomLeftChar := "."
					bottomChar := "."
					bottomRightChar := "."
					rightChar := "."
					topRightChar := "."

					if number.row-1 >= 0 {
						topChar = string(engine[number.row-1][number.col])
					}
					if number.row-1 >= 0 && number.col-1 >= 0 {
						topLeftChar = string(engine[number.row-1][number.col-1])
					}
					if number.col-1 >= 0 {
						leftChar = string(engine[number.row][number.col-1])
					}
					if number.row+1 < len(engine) && number.col-1 >= 0 {
						bottomLeftChar = string(engine[number.row+1][number.col-1])
					}
					if number.row+1 < len(engine) {
						bottomChar = string(engine[number.row+1][number.col])
					}
					if number.row+1 < len(engine) && number.col+1 < len(ligne) {
						bottomRightChar = string(engine[number.row+1][number.col+1])
					}

					if number.col+1 < len(ligne) {
						rightChar = string(engine[number.row][number.col+1])
					}

					if number.row-1 >= 0 && number.col+1 < len(ligne) {
						topRightChar = string(engine[number.row-1][number.col+1])
					}

					log.Println("topChar: ", topChar, "topLeftChar: ", topLeftChar, "leftChar: ", leftChar, "bottomLeftChar: ", bottomLeftChar, "bottomChar: ", bottomChar, "bottomRightChar: ", bottomRightChar, "rightChar: ", rightChar, "topRightChar: ", topRightChar)

					// check if the character is adjacent to a symbol except for dot and number
					if _, err := strconv.Atoi(topChar); err != nil && topChar != "." {
						isNumberAdjacentToSymbol = true
					}
					if _, err := strconv.Atoi(topLeftChar); err != nil && topLeftChar != "." {
						isNumberAdjacentToSymbol = true
					}
					if _, err := strconv.Atoi(leftChar); err != nil && leftChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if _, err := strconv.Atoi(bottomLeftChar); err != nil && bottomLeftChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if _, err := strconv.Atoi(bottomChar); err != nil && bottomChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if _, err := strconv.Atoi(bottomRightChar); err != nil && bottomRightChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if _, err := strconv.Atoi(rightChar); err != nil && rightChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if _, err := strconv.Atoi(topRightChar); err != nil && topRightChar != "." {
						isNumberAdjacentToSymbol = true
					}

					if isNumberAdjacentToSymbol {
						break
					}
				}

				if isNumberAdjacentToSymbol {
					fullNumber := ""

					for _, number := range numbersPosition {
						fullNumber += string(engine[number.row][number.col])
					}

					number, _ := strconv.Atoi(fullNumber)
					total += number
				}

				numbersPosition = []NumberPosition{}
			}
		}
	}

	log.Println(total)
}

func part2() {
	file, err := os.Open("./input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	engine := []string{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		engine = append(engine, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	total := 0

	numbersPosition := []NumberPosition{}

	numbersByRowCol := map[int]map[int][]int{}
	gearSymbols := "*"

	for row, ligne := range engine {
		for col, char := range ligne {
			_, err := strconv.Atoi(string(char))

			if err == nil {
				numbersPosition = append(numbersPosition, NumberPosition{row, col})
			} else {
				isGearAdjacentToNumber := false
				gearPosition := NumberPosition{}

				for _, number := range numbersPosition {

					if number.row-1 >= 0 && string(engine[number.row-1][number.col]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row - 1, number.col}
						break
					}
					if number.row-1 >= 0 && number.col-1 >= 0 && string(engine[number.row-1][number.col-1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row - 1, number.col - 1}
						break
					}
					if number.col-1 >= 0 && string(engine[number.row][number.col-1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row, number.col - 1}
						break
					}
					if number.row+1 < len(engine) && number.col-1 >= 0 && string(engine[number.row+1][number.col-1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row + 1, number.col - 1}
						break
					}
					if number.row+1 < len(engine) && string(engine[number.row+1][number.col]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row + 1, number.col}
						break
					}
					if number.row+1 < len(engine) && number.col+1 < len(ligne) && string(engine[number.row+1][number.col+1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row + 1, number.col + 1}
						break
					}

					if number.col+1 < len(ligne) && string(engine[number.row][number.col+1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row, number.col + 1}
						break
					}

					if number.row-1 >= 0 && number.col+1 < len(ligne) && string(engine[number.row-1][number.col+1]) == gearSymbols {
						isGearAdjacentToNumber = true
						gearPosition = NumberPosition{number.row - 1, number.col + 1}
						break
					}

				}

				if isGearAdjacentToNumber {
					fullNumber := ""

					for _, number := range numbersPosition {
						fullNumber += string(engine[number.row][number.col])
					}

					number, _ := strconv.Atoi(fullNumber)

					if numbersByRowCol[gearPosition.row] == nil {
						numbersByRowCol[gearPosition.row] = map[int][]int{}
					}

					if numbersByRowCol[gearPosition.row][gearPosition.col] == nil {
						numbersByRowCol[gearPosition.row][gearPosition.col] = []int{}
					}

					numbersByRowCol[gearPosition.row][gearPosition.col] = append(numbersByRowCol[gearPosition.row][gearPosition.col], number)

					if len(numbersByRowCol[gearPosition.row][gearPosition.col]) == 2 {
						total += numbersByRowCol[gearPosition.row][gearPosition.col][0] * numbersByRowCol[gearPosition.row][gearPosition.col][1]

					}
				}

				numbersPosition = []NumberPosition{}
			}
		}
	}

	log.Println(total)

}

func main() {
	part1()
	part2()
}
