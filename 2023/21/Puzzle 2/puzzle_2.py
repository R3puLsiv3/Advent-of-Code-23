import numpy as np


def main():
    # This puzzle was solved by looking at different intermediate results!!
    # First check after how many steps a new start point is reached. This happens to be 131 steps for all start points
    # in the up/down/left/right direction. Input is designed so that no new quadrant even gets reached in 131 steps
    # other than these 4. Now I checked every 131st result to find a pattern. By looking at the distribution of hits,
    # and a lot of trial and error in a calculator, I found that the formula
    # i^2*7262 + i^2*7232 + i*197 - (i-1)
    # yields the correct result for all i that I checked. Luckily this pattern holds.
    # 26501365 div 131 is 202300, so I calculate the value for i=202300. Let's call this value res.
    # Since 26501365 mod 131 is 65 I then checked for patterns in every (131*i+65). result up to i = 4.
    # It appears that the formula
    # res + i*7232*2 + 3725 + i*16 + (i-1)
    # calculates the correct number, where 3725 is the number of tiles reached after 65 steps.
    # The whole formula can thus be reduced to
    # (i^2)*7262 + (i^2 + 2*i)*7232 + i*213 + 3725
    # where the solution to the puzzle is found for i=202300.

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
    steps = 262
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

        if i % 131 == 0:
            hits = np.zeros((len_row, len_col), dtype=int)

            upper_matrix = np.zeros((len_row, len_col), dtype=int)
            lower_matrix = np.zeros((len_row, len_col), dtype=int)
            right_matrix = np.zeros((len_row, len_col), dtype=int)
            left_matrix = np.zeros((len_row, len_col), dtype=int)
            upper_right_matrix = np.zeros((len_row, len_col), dtype=int)
            upper_left_matrix = np.zeros((len_row, len_col), dtype=int)
            lower_right_matrix = np.zeros((len_row, len_col), dtype=int)
            lower_left_matrix = np.zeros((len_row, len_col), dtype=int)
            middle_matrix = np.zeros((len_row, len_col), dtype=int)

            for current_pos in start_positions:
                current_row = current_pos[0]
                current_col = current_pos[1]

                row = current_row % len_row
                col = current_col % len_col

                if 0 <= current_row < len_row and 0 <= current_col < len_col:
                    middle_matrix[row][col] = 1
                elif -len_row <= current_row < 0 and 0 <= current_col < len_col:
                    upper_matrix[row][col] = 1
                elif len_row <= current_row < 2*len_row and 0 <= current_col < len_col:
                    lower_matrix[row][col] = 1
                elif 0 <= current_row < len_row and -len_col <= current_col < 0:
                    left_matrix[row][col] = 1
                elif 0 <= current_row < len_row and len_col <= current_col < 2*len_col:
                    right_matrix[row][col] = 1
                elif -len_row <= current_row < 0 and -len_col <= current_col < 0:
                    upper_left_matrix[row][col] = 1
                elif -len_row <= current_row < 0 and len_col <= current_col < 2*len_col:
                    upper_right_matrix[row][col] = 1

                elif len_row <= current_row < 2*len_row and -len_col <= current_col < 0:
                    lower_left_matrix[row][col] = 1

                elif len_row <= current_row < 2*len_row and len_col <= current_col < 2*len_col:
                    lower_right_matrix[row][col] = 1

                hits[row][col] += 1

            # print(np.sum(middle_matrix))
            # print(np.sum(upper_matrix))
            # print(np.sum(lower_matrix))
            # print(np.sum(right_matrix))
            # print(np.sum(left_matrix))
            # print(np.sum(upper_right_matrix))
            # print(np.sum(upper_right_matrix))
            # print(np.sum(lower_right_matrix))
            # print(np.sum(lower_left_matrix))

            # print(hits)
            # print(np.sum(hits))
            # print(i)

    print((202300**2)*7262 + (202300**2 + 2*202300)*7232 + 202300*213 + 3725)


if __name__ == '__main__':
    main()
