import pathlib


filePath = pathlib.Path("Days/day3/input.txt")

file = open(filePath, "r")
backpacks = list(map(lambda x: x.strip(), file.readlines()))

#1                     
#vvMQnwwvrwWNfr tZJfppmSfJSmSg

ascii_a = ord("a")
ascii_z = ord("z")
ascii_A = ord("A")
ascii_Z = ord("Z")

total = 0

for backpack in backpacks:
    middle = len(backpack) // 2
    container1 = backpack[0:middle]
    container2 = backpack[middle:len(backpack)]
    for item1 in container1:
        if (item1 not in container2):
            continue
        if (ascii_a <= ord(item1) <= ascii_z):
            total += ord(item1) - ascii_a + 1
            break
        else:
            total += ord(item1) - ascii_A + 27
            break


print(total)

total_2 = 0
for i in range(0, len(backpacks), 3):
   common = set(backpacks[i]).intersection(set(backpacks[i + 1])).intersection(set(backpacks[i + 2])).pop()
       
   if (ascii_a <= ord(common) <= ascii_z):
        total_2 += ord(common) - ascii_a + 1
   else:
        total_2 += ord(common) - ascii_A + 27

print(total_2)
