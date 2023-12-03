import pathlib
import math
from node import Node

part_1_total = 0
part_2_min_total = math.inf

def part_1(root: Node):
    current_directory_size = 0
    for child in root.children:
        if (child.type == "file"):
           current_directory_size += child.size
        else:
          current_directory_size += part_1(child)
    
    if (current_directory_size <= 100000):
        global part_1_total
        part_1_total += current_directory_size

    root.size = current_directory_size
    return current_directory_size

def part_2(root: Node, free_space: int):
    if (free_space + root.size >= 30000000):
        global part_2_min_total
        part_2_min_total = min(part_2_min_total, root.size)
    
    for child in root.children:
        if (child.type == "file"):
            continue
        part_2(child, free_space)

file_path = pathlib.Path("Days/day7/input.txt")
file = open(file_path, "r")
histories = list(map(lambda x: x.strip(), file.readlines()))
file.close()

first_element = histories.pop(0).split(" ")

root = Node(first_element[2], "directory")

trace_current_directory = [root]
current_node = trace_current_directory[0]

for history in histories:
    content = history.split(" ")

    if (content[1] == "ls"):
        continue
    elif (len(content) == 3 and content[1] == "cd" ):
        if content[2] == "/":
            trace_current_directory.clear()
            trace_current_directory.append(root)
            current_node = trace_current_directory[0]
        elif content[2] == "..":
            trace_current_directory.pop(-1)
            current_node = trace_current_directory[-1]
        else:
            trace_current_directory.append(current_node.find_child_by_name(content[2]))
            current_node = trace_current_directory[-1]
    elif (content[0] == "dir"):
        current_node.add_child(Node(content[1], "directory"))
    else:
        current_node.add_child(Node(content[1], "file", int(content[0])))


part_1(root)
print(part_1_total)

free_space = 70000000 - root.size
part_2(root, free_space)
print(part_2_min_total)