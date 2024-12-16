
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    warehouse = []
    moves = ""
    upper_part = True
    lower_part = False
    for line in lines:
        if line == "":
            upper_part = False
            lower_part = True
        if upper_part:
            warehouse.append(list(line))
        if lower_part:
            moves += line

    row_robot, col_robot = [(row, col) for row, line in enumerate(warehouse) for col, char in enumerate(line) if char == "@"].pop()

    directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    for move in moves:
        row_delta, col_delta = directions[move]

        next_row = row_robot + row_delta
        next_col = col_robot + col_delta
        match warehouse[next_row][next_col]:
            case ".":
                warehouse[row_robot][col_robot] = "."
                row_robot, col_robot = (next_row, next_col)
                warehouse[row_robot][col_robot] = "@"
            case "#":
                pass
            case "O":
                to_move = 1
                while True:
                    next_row += row_delta
                    next_col += col_delta

                    match warehouse[next_row][next_col]:
                        case "#":
                            break
                        case "O":
                            to_move += 1
                        case ".":
                            while to_move != 0:
                                warehouse[next_row][next_col] = "O"
                                next_row -= row_delta
                                next_col -= col_delta
                                to_move -= 1
                            warehouse[row_robot][col_robot] = "."
                            row_robot, col_robot = next_row, next_col
                            warehouse[row_robot][col_robot] = "@"
                            break

    print(sum([100 * row + col for row, line in enumerate(warehouse) for col, char in enumerate(line) if char == "O"]))

if __name__ == '__main__':
    main()
