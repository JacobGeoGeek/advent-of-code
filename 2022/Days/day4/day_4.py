import pathlib


file_path = pathlib.Path("Days/day4/input.txt")
file = open(file_path, "r")
sections = list(map(lambda x: x.strip(), file.readlines()))

number_of_fully_contain = 0

for section in sections:
    groups = section.split(",")
    elf_1 = list(map(lambda x: int(x), groups[0].split("-")))
    elf_2 = list(map(lambda x: int(x), groups[1].split("-")))


    if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]):
        number_of_fully_contain += 1
    elif (elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]):
        number_of_fully_contain += 1

print(number_of_fully_contain)

number_of_overlap = 0

for section in sections:
    groups = section.split(",")
    elf_1 = list(map(lambda x: int(x), groups[0].split("-")))
    elf_2 = list(map(lambda x: int(x), groups[1].split("-")))

    ids = list(range(elf_1[0], elf_1[1] + 1))
  
    for i in range(elf_2[0], elf_2[1] + 1):
        if (i in ids):
            number_of_overlap += 1
            break


print(number_of_overlap)
