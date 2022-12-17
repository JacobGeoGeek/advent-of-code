import pathlib
from functools import reduce

file_path = pathlib.Path("Days/day8/input.txt")
file = open(file_path, "r")
trees_grid = list(map(lambda x: list(map(lambda y: int(y), x.strip())), file.readlines()))
file.close()


def count_edges(grid) -> int:
    return (len(grid[0]) * 2) + ((len(grid) - 2) * 2)

def is_visible(grid, row, col) -> bool:
    left = grid[row][:col]
    right = grid[row][col + 1:]
    top = [tree[col] for tree in grid[:row][::-1]]
    bottom = [tree[col] for tree in grid[row + 1:]]
    if (grid[row][col] > max(top)):
        return True
    if (grid[row][col] > max(bottom)):
        return True
    if (grid[row][col] > max(left)):
        return True
    if (grid[row][col] > max(right)):
        return True
    return False

def calc_scenic_score(grid, row, col) -> int:
    scenic_score_direction = [0] * 4 # score are left, top, right and bottom

    left = grid[row][:col]
    right = grid[row][col + 1:]
    top = [tree[col] for tree in grid[:row][::-1]]
    bottom = [tree[col] for tree in grid[row + 1:]]

    for i in range(len(left) - 1, -1, -1):
        if (left[i] >= grid[row][col]):
            scenic_score_direction[0] += 1
            break
        else:
            scenic_score_direction[0] += 1
    
    for i in range(0, len(top)):
        if (top[i] >= grid[row][col]):
          scenic_score_direction[1] += 1
          break
        else:
          scenic_score_direction[1] += 1
    
    for i in range(0, len(right)):
         if (right[i] >= grid[row][col]):
           scenic_score_direction[2] += 1
           break
         else:
           scenic_score_direction[2] += 1
    
    for i in range(0, len(bottom)):
         if (bottom[i] >= grid[row][col]):
           scenic_score_direction[3] += 1
           break
         else:
           scenic_score_direction[3] += 1

    return reduce(lambda x, y: x * y, scenic_score_direction)



def part_1(grid) -> int:
    total = 0
    total += count_edges(grid)

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if (is_visible(grid, row, col)):
                total += 1
    return total

def part_2(grid) -> int:
    highest_scenic_score = 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            total =  calc_scenic_score(grid, row, col)
            print(f"row: {row}, col: {col}, total: {total}")
            if total > highest_scenic_score:
                highest_scenic_score = total

    return highest_scenic_score

print(part_1(trees_grid))
print(part_2(trees_grid))