
def main():
    with open("input.txt") as f:
        data = f.read()

    lines = data.splitlines()

    directions = []
    lengths = []
    for line in lines:
        values = line.split()
        directions.append(values[0])
        lengths.append(int(values[1]))

    row = 0
    col = 0
    outline = {}
    for i in range(len(lines)):
        match directions[i]:
            case "L":
                for _ in range(lengths[i]):
                    col -= 1
                    outline[(row, col)] = True
            case "R":
                for _ in range(lengths[i]):
                    col += 1
                    outline[(row, col)] = True
            case "U":
                for _ in range(lengths[i]):
                    row -= 1
                    outline[(row, col)] = True
            case "D":
                for _ in range(lengths[i]):
                    row += 1
                    outline[(row, col)] = True

    inside = [(1, 1)]
    while inside:
        current_trench = inside.pop()
        current_row = current_trench[0]
        current_col = current_trench[1]
        outline[current_trench] = True
        if not (current_row + 1, current_col) in outline:
            inside.append((current_row + 1, current_col))
        if not (current_row - 1, current_col) in outline:
            inside.append((current_row - 1, current_col))
        if not (current_row, current_col + 1) in outline:
            inside.append((current_row, current_col + 1))
        if not (current_row, current_col - 1) in outline:
            inside.append((current_row, current_col - 1))

    print(len(outline) + len(inside))


if __name__ == '__main__':
    main()
