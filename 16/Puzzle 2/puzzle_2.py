import sys


def count_energized(lines, start_pos, direction, energized):
    i = start_pos[0]
    j = start_pos[1]
    row_len = len(lines[0])
    column_len = len(lines)
    if start_pos in energized and direction in energized[start_pos]:
        return
    elif not 0 <= i < row_len or not 0 <= j < column_len:
        return
    else:
        energized[start_pos].append(direction)

    match direction:
        case "Right":
            match lines[i][j]:
                case ".":
                    count_energized(lines, (i, j+1), "Right", energized)
                case "/":
                    count_energized(lines, (i-1, j), "Up", energized)
                case "\\":
                    count_energized(lines, (i+1, j), "Down", energized)
                case "|":
                    count_energized(lines, (i-1, j), "Up", energized)
                    count_energized(lines, (i+1, j), "Down", energized)
                case "-":
                    count_energized(lines, (i, j+1), "Right", energized)
        case "Left":
            match lines[i][j]:
                case ".":
                    count_energized(lines, (i, j-1), "Left", energized)
                case "/":
                    count_energized(lines, (i+1, j), "Down", energized)
                case "\\":
                    count_energized(lines, (i-1, j), "Up", energized)
                case "|":
                    count_energized(lines, (i-1, j), "Up", energized)
                    count_energized(lines, (i+1, j), "Down", energized)
                case "-":
                    count_energized(lines, (i, j-1), "Left", energized)
        case "Up":
            match lines[i][j]:
                case ".":
                    count_energized(lines, (i-1, j), "Up", energized)
                case "/":
                    count_energized(lines, (i, j+1), "Right", energized)
                case "\\":
                    count_energized(lines, (i, j-1), "Left", energized)
                case "|":
                    count_energized(lines, (i-1, j), "Up", energized)
                case "-":
                    count_energized(lines, (i, j+1), "Right", energized)
                    count_energized(lines, (i, j-1), "Left", energized)
        case "Down":
            match lines[i][j]:
                case ".":
                    count_energized(lines, (i+1, j), "Down", energized)
                case "/":
                    count_energized(lines, (i, j-1), "Left", energized)
                case "\\":
                    count_energized(lines, (i, j+1), "Right", energized)
                case "|":
                    count_energized(lines, (i+1, j), "Down", energized)
                case "-":
                    count_energized(lines, (i, j+1), "Right", energized)
                    count_energized(lines, (i, j-1), "Left", energized)


def main():
    sys.setrecursionlimit(10000)

    with open("input.txt") as f:
        data = f.read()

    lines = data.split()

    results = []
    for row_len in range(len(lines)):
        energized = {}
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                energized[(i, j)] = []

        count_energized(lines, (row_len, 0), "Right", energized)

        result = 0
        for tile in energized:
            if energized[tile]:
                result += 1
        results.append(result)

    for row_len in range(len(lines)):
        energized = {}
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                energized[(i, j)] = []

        count_energized(lines, (row_len, len(lines[0]) - 1), "Left", energized)

        result = 0
        for tile in energized:
            if energized[tile]:
                result += 1
        results.append(result)

    for col_len in range(len(lines[0])):
        energized = {}
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                energized[(i, j)] = []

        count_energized(lines, (0, col_len), "Down", energized)

        result = 0
        for tile in energized:
            if energized[tile]:
                result += 1
        results.append(result)

    for col_len in range(len(lines)):
        energized = {}
        for i, row in enumerate(lines):
            for j, char in enumerate(row):
                energized[(i, j)] = []

        count_energized(lines, (len(lines) - 1, col_len), "Up", energized)

        result = 0
        for tile in energized:
            if energized[tile]:
                result += 1
        results.append(result)

    print(max(results))


if __name__ == '__main__':
    main()
