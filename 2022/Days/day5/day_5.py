import pathlib

def part_1(stacks, moves):
    for move in moves:
        quantity =  int(move[1])
        source = int(move[3]) - 1
        destination = int(move[5]) - 1

        for i in range(0, quantity):
            stacks[destination].append(stacks[source].pop())

    top_crates = ""

    for stack in stacks:
        top_crates += stack[-1]
    return top_crates

def part_2(stacks, moves):
    for move in moves:
        quantity =  int(move[1])
        source = int(move[3]) - 1
        destination = int(move[5]) - 1

        stack_index = len(stacks[source]) - quantity
        end_index = len(stacks[source])
        
        for i in range(stack_index, end_index):
            stacks[destination].append(stacks[source][i])
        
        for i in range(0, quantity):
            stacks[source].pop()
        
    top_crates_9001 = ""
        
    for stack in stacks:
        top_crates_9001 += stack[-1]
    return top_crates_9001

file_path = pathlib.Path("Days/day5/moves.txt")

file = open(file_path, "r")
moves = list(map(lambda x: x.strip().split(" "), file.readlines()))

#             [J] [Z] [G]            
#             [Z] [T] [S] [P] [R]    
# [R]         [Q] [V] [B] [G] [J]    
# [W] [W]     [N] [L] [V] [W] [C]    
# [F] [Q]     [T] [G] [C] [T] [T] [W]
# [H] [D] [W] [W] [H] [T] [R] [M] [B]
# [T] [G] [T] [R] [B] [P] [B] [G] [G]
# [S] [S] [B] [D] [F] [L] [Z] [N] [L]
#  1   2   3   4   5   6   7   8   9 

init_stacks = [
    ["S", "T", "H", "F", "W", "R"],
    ["S", "G", "D", "Q", "W"],
    ["B", "T", "W"],
    ["D", "R", "W", "T", "N", "Q", "Z", "J"],
    ["F", "B", "H", "G", "L", "V", "T", "Z"],
    ["L", "P", "T", "C", "V", "B", "S", "G"],
    ["Z", "B", "R", "T", "W", "G", "P"],
    ["N", "G", "M", "T", "C", "J", "R"],
    ["L", "G", "B", "W"]
]


print(part_1(init_stacks, moves))
print(part_2(init_stacks, moves))

