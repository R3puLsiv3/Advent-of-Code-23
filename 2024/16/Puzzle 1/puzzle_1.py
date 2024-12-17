import numpy as np
from queue import PriorityQueue
from itertools import count

class Position:
    def __init__(self, position, direction):
        self.row = position[0]
        self.col = position[1]
        self.position = position
        self.direction = direction

def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    start, end = (0, 0), (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)

    direction = (0, 1)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    turns = {(0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)], (1, 0): [(0, 1), (0, -1)], (-1, 0): [(0, 1), (0, -1)]}

    current = Position(start, direction)
    queue = PriorityQueue()

    # Necessary because queue can't compare objects if the priority is the same.
    unique = count()
    queue.put((0, next(unique), current))

    done = {}
    dists = {((i, j), direction): np.inf for i, line in enumerate(lines) for j, char in enumerate(line) for direction in directions if char != "#"}
    dists[start, direction] = 0

    while not queue.empty():
        dist, _, current = queue.get()
        if current.position == end:
            print(dist)
            break
        done[current.position, current.direction] = True

        neighbors = [Position(current.position, direction) for direction in turns[current.direction]]
        next_row = current.row + current.direction[0]
        next_col = current.col + current.direction[1]
        if lines[next_row][next_col] != "#":
            next_pos = (next_row, next_col)
            neighbors.append(Position(next_pos, current.direction))

        for neighbor in neighbors:
            if (neighbor.position, neighbor.direction) in done:
                continue
            if current.position != neighbor.position:
                new_dist = dists[current.position, current.direction] + 1
            else:
                new_dist = dists[current.position, current.direction] + 1000

            if new_dist < dists[neighbor.position, neighbor.direction]:
                dists[neighbor.position, neighbor.direction] = new_dist
            queue.put((new_dist, next(unique), neighbor))


if __name__ == '__main__':
    main()
