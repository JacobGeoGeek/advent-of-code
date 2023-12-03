import pathlib
import math
from motion import Motion

UP: str = "U"
DOWN: str = "D"
LEFT: str = "L"
RIGHT: str = "R"

file_path = pathlib.Path("Days/day9/input.txt")
file = open(file_path, "r")

series_motions: list[str] = list(map(lambda item: item.strip(), file.readlines()))
file.close()

def number_position_tail_visited(knots: list[int]) -> int:
    visited_coordinates: set[tuple[int, int]] = set()
    visited_coordinates.add((0, 0))
    for item in series_motions:
        motion: Motion = Motion(item.split(" ")[0], item.split(" ")[1])

        move_x = 0
        move_y = 0
        
        if motion.direction == UP:
            move_y = 1
        elif motion.direction == DOWN:
            move_y = -1
        elif motion.direction == LEFT:
            move_x = -1
        else:
            move_x = 1
    
        for i in range(1, motion.step + 1):
            knots[0][0] += move_x
            knots[0][1] += move_y
            for i in range(1, len(knots)):
                head = knots[i - 1]
                tail = knots[i]

                if (head[0] == tail[0]):
                    dy: int = head[1] - tail[1]
                    if (abs(dy) > 1):
                        tail[1] += int(math.copysign(1, dy))
                elif (head[1] == tail[1]):
                   dx: int = head[0] - tail[0]
                   if (abs(dx) > 1):
                     tail[0] += int(math.copysign(1, dx))
                else:
                    dx: int = head[0] - tail[0]
                    dy: int = head[1] - tail[1]
                    if abs(dx) > 1 or abs(dy) > 1:
                        tail[0] += int(math.copysign(1, dx))
                        tail[1] += int(math.copysign(1, dy))

            visited_coordinates.add(tuple(knots[-1]))
    return len(visited_coordinates)

two_knots = [[0, 0], [0, 0]]
ten_knots = [[0, 0] for i in range(0, 10)]

print(number_position_tail_visited(two_knots))
print(number_position_tail_visited(ten_knots))



