package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0
	for scanner.Scan() {
		text := scanner.Text()

		startIndex := 0
		endIndex := len(text) - 1

		firstDigitIndex := -1
		lastDigitIndex := -1

		for startIndex < len(text) || endIndex > -1 {
			if firstDigitIndex == -1 {
				_, err := strconv.Atoi(string(text[startIndex]))

				if err == nil {
					firstDigitIndex = startIndex
				}
			}

			if lastDigitIndex == -1 {
				_, err := strconv.Atoi(string(text[endIndex]))

				if err == nil {
					lastDigitIndex = endIndex
				}
			}

			if firstDigitIndex != -1 && lastDigitIndex != -1 {
				break
			}

			startIndex++
			endIndex--
		}

		number, err := strconv.Atoi(string(text[firstDigitIndex]) + string(text[lastDigitIndex]))

		if err != nil {
			log.Fatal(err)
		} else {
			total += number
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(total)
}
