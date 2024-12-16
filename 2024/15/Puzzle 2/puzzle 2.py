import numpy as np

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

    wide_warehouse = []
    for row in warehouse:
        wider_row = []
        for char in row:
            match char:
                case "@":
                    wider_row.append(char)
                    wider_row.append(".")
                case "#":
                    wider_row.append(char)
                    wider_row.append(char)
                case "O":
                    wider_row.append("[")
                    wider_row.append("]")
                case ".":
                    wider_row.append(char)
                    wider_row.append(char)
        wide_warehouse.append(wider_row)

    row_robot, col_robot = [(row, col) for row, line in enumerate(wide_warehouse) for col, char in enumerate(line) if char == "@"].pop()

    directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    for move in moves:
        row_delta, col_delta = directions[move]

        next_row = row_robot + row_delta
        next_col = col_robot + col_delta
        match wide_warehouse[next_row][next_col]:
            case ".":
                wide_warehouse[row_robot][col_robot] = "."
                row_robot, col_robot = (next_row, next_col)
                wide_warehouse[row_robot][col_robot] = "@"
            case "#":
                pass
            case "[":
                if move == ">":
                    to_move = 1
                    while True:
                        next_col += 2 * col_delta

                        match wide_warehouse[next_row][next_col]:
                            case "#":
                                break
                            case "[":
                                to_move += 1
                            case ".":
                                while to_move != 0:
                                    wide_warehouse[next_row][next_col] = "]"
                                    wide_warehouse[next_row][next_col - 1] = "["
                                    next_col -= 2 * col_delta
                                    to_move -= 1
                                wide_warehouse[row_robot][col_robot] = "."
                                col_robot = next_col
                                wide_warehouse[row_robot][col_robot] = "@"
                                break
                else:
                    total_boxes = {(next_row, next_col, "["), (next_row, next_col + 1, "]")}
                    seen ={}
                    moveable = True
                    boxes = [(next_row, next_col), (next_row, next_col + 1)]
                    while boxes:
                        row, col = boxes.pop()
                        if (row, col) in seen:
                            continue
                        seen[(row, col)] = True
                        row, col = row + row_delta, col + col_delta
                        match wide_warehouse[row][col]:
                            case "#":
                                moveable = False
                                break
                            case ".":
                                continue
                            case "[":
                                boxes.append((row, col))
                                total_boxes.add((row, col, "["))
                                boxes.append((row, col + 1))
                                total_boxes.add((row, col +1, "]"))
                            case "]":
                                boxes.append((row, col))
                                total_boxes.add((row, col, "]"))
                                boxes.append((row, col - 1))
                                total_boxes.add((row, col - 1, "["))
                    if moveable:
                        if move == "^":
                            total_boxes = sorted(total_boxes, key=lambda x: x[0])
                        else:
                            total_boxes = sorted(total_boxes, key=lambda x: x[0], reverse=True)
                        for row, col, char in total_boxes:
                            wide_warehouse[row][col] = "."
                            wide_warehouse[row + row_delta][col] = char
                        wide_warehouse[row_robot][col_robot] = "."
                        row_robot += row_delta
                        wide_warehouse[row_robot][col_robot] = "@"

            case "]":
                if move == "<":
                    to_move = 1
                    while True:
                        next_col += 2 * col_delta
                        match wide_warehouse[next_row][next_col]:
                            case "#":
                                break
                            case "]":
                                to_move += 1
                            case ".":
                                while to_move != 0:
                                    wide_warehouse[next_row][next_col] = "["
                                    wide_warehouse[next_row][next_col + 1] = "]"
                                    next_col -= 2 * col_delta
                                    to_move -= 1
                                wide_warehouse[row_robot][col_robot] = "."
                                col_robot = next_col
                                wide_warehouse[row_robot][col_robot] = "@"
                                break
                else:
                    total_boxes = {(next_row, next_col, "]"), (next_row, next_col - 1, "[")}
                    seen = {}
                    moveable = True
                    boxes = [(next_row, next_col), (next_row, next_col - 1)]
                    while boxes:
                        row, col = boxes.pop()
                        if (row, col) in seen:
                            continue
                        seen[(row, col)] = True
                        row, col = row + row_delta, col + col_delta
                        match wide_warehouse[row][col]:
                            case "#":
                                moveable = False
                                break
                            case ".":
                                continue
                            case "[":
                                boxes.append((row, col))
                                total_boxes.add((row, col, "["))
                                boxes.append((row, col + 1))
                                total_boxes.add((row, col + 1, "]"))
                            case "]":
                                boxes.append((row, col))
                                total_boxes.add((row, col, "]"))
                                boxes.append((row, col - 1))
                                total_boxes.add((row, col - 1, "["))
                    if moveable:
                        if move == "^":
                            total_boxes = sorted(total_boxes, key=lambda x: x[0])
                        else:
                            total_boxes = sorted(total_boxes, key=lambda x: x[0], reverse=True)
                        for row, col, char in total_boxes:
                            wide_warehouse[row][col] = "."
                            wide_warehouse[row + row_delta][col] = char
                        wide_warehouse[row_robot][col_robot] = "."
                        row_robot += row_delta
                        wide_warehouse[row_robot][col_robot] = "@"

    print(sum([100 * row + col for row, line in enumerate(wide_warehouse) for col, char in enumerate(line) if char == "["]))

if __name__ == '__main__':
    main()
