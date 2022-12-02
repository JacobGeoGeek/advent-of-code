import pathlib

filePath = pathlib.Path("Days/day1/input.txt")
file = open(filePath, "r")
caloriesByElf = list(map(lambda x: x.replace('\n', ' ').split(" "), file.read().split("\n\n")))
file.close()

totalCaloryByElf = []

for calories in caloriesByElf:
    totalCaloryByElf.append(sum(list(map(lambda y:  int(y), filter(lambda x: len(x) > 0, calories)))))

print(max(totalCaloryByElf))

print(sum(sorted(totalCaloryByElf, reverse=True)[0:3]))