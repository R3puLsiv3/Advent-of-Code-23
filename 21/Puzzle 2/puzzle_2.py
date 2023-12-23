import numpy as np


def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    len_row = len(lines)
    len_col = len(lines[0])

    start_position = (0, 0)
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == "S":
                start_position = (i, j)

    start_positions = set()
    start_positions.add(start_position)
    steps = 550
    for i in range(1, steps + 1):
        new_start_positions = set()
        while start_positions:
            current_pos = start_positions.pop()
            current_row = current_pos[0]
            current_col = current_pos[1]

            row = current_row % len_row
            col = current_col % len_col

            next_row = (current_row - 1) % len_row
            if lines[next_row][col] != "#":
                new_start_positions.add((current_row - 1, current_col))

            next_row = (current_row + 1) % len_row
            if lines[next_row][col] != "#":
                new_start_positions.add((current_row + 1, current_col))

            next_col = (current_col - 1) % len_col
            if lines[row][next_col] != "#":
                new_start_positions.add((current_row, current_col - 1))

            next_col = (current_col + 1) % len_col
            if lines[row][next_col] != "#":
                new_start_positions.add((current_row, current_col + 1))

        start_positions = new_start_positions

        if i % 55 == 0:
            hits = np.zeros((len_row, len_col), dtype=int)

            for current_pos in start_positions:
                current_row = current_pos[0]
                current_col = current_pos[1]

                row = current_row % len_row
                col = current_col % len_col

                hits[row][col] += 1
            print(hits)
            print(np.sum(hits))
            print(i)

    hits = np.zeros((len_row, len_col), dtype=int)

    for current_pos in start_positions:
        current_row = current_pos[0]
        current_col = current_pos[1]

        row = current_row % len_row
        col = current_col % len_col

        hits[row][col] += 1
    print(hits)

    occurrences = {30: 0, 28: 0, 25: 0, 24: 0, 22: 0, 20: 0, 16: 0, 0: 0}
    #for row in hits:
    #    for num in row:
    #        occurrences[num] += 1

    k = 481843
    print(occurrences)
    val_30 = (5*k)**2 + 5*k
    val_28 = (5*k)**2 + 5*k - 2
    val_25 = (5*k)**2
    val_24 = (5*k)**2 - 1
    val_22 = (5*k)**2 - 3
    val_20 = (5*k)**2 - 5*k
    val_16 = (5*k - 1)**2

    result = val_30 * occurrences[30] + val_28 * occurrences[28] + val_25 * occurrences[25] + val_24 * occurrences[24] +\
             val_22 * occurrences[22] + val_20 * occurrences[20] + val_16 * occurrences[16]

    print(result)


if __name__ == '__main__':
    main()
