package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func par1() {
	RED_MAX := 12
	GREEN_MAX := 13
	BLUE_MAX := 14

	file, err := os.Open("./input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		game := strings.Split(scanner.Text(), ":")

		gameIndex, err := strconv.Atoi(strings.Split(game[0], " ")[1])

		if err != nil {
			log.Fatal(err)
		}

		gameSets := strings.Split(game[1], ";")

		isGameSetValid := true

		for _, gameSet := range gameSets {
			gameSetValues := strings.Split(gameSet, ",")

			// check if the game set contains the red or blue or green

			for _, gameSetValue := range gameSetValues {
				info := strings.Split(strings.TrimSpace(gameSetValue), " ")

				if info[1] == "red" {
					red, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if red > RED_MAX {
						isGameSetValid = false
						break
					}
				} else if info[1] == "blue" {
					blue, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if blue > BLUE_MAX {
						isGameSetValid = false
						break
					}

				} else if info[1] == "green" {
					green, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if green > GREEN_MAX {
						isGameSetValid = false
						break
					}
				}
			}

			if !isGameSetValid {
				break
			}

		}

		if isGameSetValid {
			total += gameIndex
		}
		gameIndex++
	}
	fmt.Println(total)
}

func par2() {

	file, err := os.Open("./input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		maxRedPlayed := -1
		maxGreenPlayed := -1
		maxBluePlayed := -1

		game := strings.Split(scanner.Text(), ":")

		gameSets := strings.Split(game[1], ";")

		for _, gameSet := range gameSets {

			gameSetValues := strings.Split(gameSet, ",")

			for _, gameSetValue := range gameSetValues {
				info := strings.Split(strings.TrimSpace(gameSetValue), " ")

				if info[1] == "red" {
					red, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if red > maxRedPlayed {
						maxRedPlayed = red
					}
				} else if info[1] == "blue" {
					blue, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if blue > maxBluePlayed {
						maxBluePlayed = blue
					}

				} else if info[1] == "green" {
					green, err := strconv.Atoi(string(info[0]))

					if err != nil {
						log.Fatal(err)
					}

					if green > maxGreenPlayed {
						maxGreenPlayed = green
					}
				}
			}

		}
		total += maxRedPlayed * maxBluePlayed * maxGreenPlayed
	}
	fmt.Println(total)
}

func main() {
	par1()
	par2()
}
