from queue import PriorityQueue
import numpy as np


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")

    length = 71

    bytes_pos = [tuple(map(int, line.split(","))) for line in lines]
    memory_space = [["." for _ in range(length)] for _ in range(length)]
    for row, col in bytes_pos[:1024]:
        memory_space[row][col] = "#"

    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    memory_space = [["#"] * (length + 2 * padding)] * padding + [["#"] * padding + line + ["#"] * padding for line in
                                                               memory_space] + [["#"] * (length + 2 * padding)] * padding

    # This could be made more efficient by some kind of binary search and BFS instead of Dijkstra
    for i in range(1024, len(bytes_pos)):
        queue = PriorityQueue()
        start = (1, 1)
        end = (71, 71)
        queue.put((0, start))

        new_byte_row, new_byte_col = bytes_pos[i]
        memory_space[new_byte_row + 1][new_byte_col + 1] = "#"

        done = {}
        dists = {(i, j): np.inf for i, line in enumerate(memory_space) for j, char in enumerate(line) if char != "#"}
        dists[start] = 0

        is_possible = False
        while not queue.empty():
            dist, current = queue.get()
            if current == end:
                is_possible = True
                break
            row = current[0]
            col = current[1]

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for neighbor in neighbors:
                row = neighbor[0]
                col = neighbor[1]
                if neighbor in done or memory_space[row][col] == "#":
                    continue
                done[neighbor] = True

                new_dist = dist + 1
                if new_dist < dists[neighbor]:
                    dists[neighbor] = new_dist
                queue.put((new_dist, neighbor))

        if not is_possible:
            print(f"{bytes_pos[i][0]},{bytes_pos[i][1]}")
            break


if __name__ == '__main__':
    main()
