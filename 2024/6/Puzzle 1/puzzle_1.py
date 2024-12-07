
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.split("\n")
    length = len(lines[0])
    padding = 1
    # Add padding so it's not necessary to check for boundaries later.
    lines = ["X" * (length + 2 * padding)] * padding + ["X" * padding + line + "X" * padding for line in lines] + [
        "X" * (length + 2 * padding)] * padding

    pos_guard, direction = [((row_idx, col_idx), tile) for row_idx, row in enumerate(lines) for col_idx, tile in enumerate(row) if tile in ["<", ">", "^", "v"]].pop()

    visited = set()
    while lines[pos_guard[0]][pos_guard[1]] != "X":
        visited.add(pos_guard)
        match direction:
            case "<":
                if lines[pos_guard[0]][pos_guard[1] - 1] == "#":
                    pos_guard = (pos_guard[0] - 1, pos_guard[1])
                    direction = "^"
                else:
                    pos_guard = (pos_guard[0], pos_guard[1] - 1)
            case ">":
                if lines[pos_guard[0]][pos_guard[1] + 1] == "#":
                    pos_guard = (pos_guard[0] + 1, pos_guard[1])
                    direction = "v"
                else:
                    pos_guard = (pos_guard[0], pos_guard[1] + 1)
            case "^":
                if lines[pos_guard[0] - 1][pos_guard[1]] == "#":
                    pos_guard = (pos_guard[0], pos_guard[1] + 1)
                    direction = ">"
                else:
                    pos_guard = (pos_guard[0] - 1, pos_guard[1])
            case "v":
                if lines[pos_guard[0] + 1][pos_guard[1]] == "#":
                    pos_guard = (pos_guard[0], pos_guard[1] - 1)
                    direction = "<"
                else:
                    pos_guard = (pos_guard[0] + 1, pos_guard[1])

    print(len(visited))

if __name__ == '__main__':
    main()
