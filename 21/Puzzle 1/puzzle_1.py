
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    start_position = (0, 0)
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == "S":
                start_position = (i, j)

    start_positions = set()
    start_positions.add(start_position)
    steps = 64
    for _ in range(steps):
        new_start_positions = set()
        while start_positions:
            current_pos = start_positions.pop()
            current_row = current_pos[0]
            current_col = current_pos[1]

            if current_row > 0 and lines[current_row - 1][current_col] != "#":
                new_start_positions.add((current_row - 1, current_col))
            if current_row < len(lines) - 1 and lines[current_row + 1][current_col] != "#":
                new_start_positions.add((current_row + 1, current_col))
            if current_col > 0 and lines[current_row][current_col - 1] != "#":
                new_start_positions.add((current_row, current_col - 1))
            if current_col < len(lines[0]) - 1 and lines[current_row][current_col + 1] != "#":
                new_start_positions.add((current_row, current_col + 1))

        start_positions = new_start_positions

    print(len(start_positions))


if __name__ == '__main__':
    main()
