import pathlib

def getScorePart1(opponent, me):
    if (opponent == "A" and me == "X"):
        return 4
    if (opponent == "A" and me == "Y"):
        return 8
    if (opponent == "A" and me == "Z"):
        return 3
    if (opponent == "B" and me == "X"):
        return 1
    if (opponent == "B" and me == "Y"):
        return 5
    if (opponent == "B" and me == "Z"):
        return 9
    if (opponent == "C" and me == "X"):
        return 7
    if (opponent == "C" and me == "Y"):
        return 2
    if (opponent == "C" and me == "Z"):
        return 6

def getScorePart2(opponent, me):
    if (opponent == "A" and me == "X"):
        return 3
    if (opponent == "A" and me == "Y"):
        return 4
    if (opponent == "A" and me == "Z"):
        return 8
    if (opponent == "B" and me == "X"):
        return 1
    if (opponent == "B" and me == "Y"):
        return 5
    if (opponent == "B" and me == "Z"):
        return 9
    if (opponent == "C" and me == "X"):
        return 2
    if (opponent == "C" and me == "Y"):
        return 6
    if (opponent == "C" and me == "Z"):
        return 7


filePath = pathlib.Path("Days/day2/input.txt")

file = open(filePath, "r")

lines = file.readlines()
file.close()

total = 0
total2 = 0

for line in lines:
  userValues = line.strip().split(" ")
  score1 = getScorePart1(userValues[0], userValues[1])
  score2 = getScorePart2(userValues[0], userValues[1])
  
  total += score1
  total2 += score2

print(total)
print(total2)